# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:57:13 2021

@author: arman
"""

from bottle import route, run, template,static_file, request, redirect, response,error,default_app
from down import downloadImage, resizeImgFunc, downloadCSV
import os, sys
import sqlite3
import datetime
from beaker.middleware import SessionMiddleware
 

session_opts = {
    'session.type':'file',                
    'session.timeout':3600, # login time 1 hour      
    'session.data_dir':'/tmp/sessions',  
    'sessioni.auto':True
    }
dictUser = {}
pw = ''

@error(404)
def error404(error):
    return template('notFound')

#for get file
@route('/dict/<filename>.css')
def send_css(filename):
    return static_file('{}.css'.format(filename), root='./static/assets/dist/css/')

@route('/dict/self/<filename>.css')
def send_fileCss(filename):
    return static_file('{}.css'.format(filename), root='./static/assets/dist/css/{}'.format(filename))

@route('/dict/<filename>.js')
def send_js(filename):
    return static_file('{}.js'.format(filename), root='./static/assets/dist/js/')

@route('/dict/self/<filename>.js')
def send_fileJs(filename):
    return static_file('{}.js'.format(filename), root='./static/assets/dist/js/{}'.format(filename))

@route('/dict/<filename>.png')
def send_img(filename):
    return static_file('{}.png'.format(filename), root='./static/assets/img/')

@route('/html/<filename>.html')
def send_html(filename):
    return static_file('{}.html'.format(filename), root='./views/html/')

@route('/terminology.csv')
def send_csv():
    if downloadCSV():
        return static_file('terminology.csv', root='./static/csv/')
    else:
        return '<h1>error</h1>'

# end of get file

#check and download the image to file 
@route('/find/<filename>')
def server_static(filename):
    listDir = os.listdir('./simple_images')
    #print(listDir , filename)
    if filename not in listDir: # check the file in dir
        downloadImage(filename)
    fileName = filename +".jpg"
    #client_ip = request.environ.get('REMOTE_ADDR')
    #print("Your IP:",client_ip)
    return static_file(fileName, root='./simple_images/{}'.format(filename))

#get the image file
@route('/file/<filename>')
def server_file(filename):
    name = ""
    for x in filename:
        if x != ".":
            name += x
        else:
            break
    #print(name)
    return static_file(filename, root='./simple_images/{}'.format(name))

@route('/')
def index():
    if checkLogin():
        return template('indexLogin')
    else:
        return template('index')
@route('/login')
def login():
    return template('views/login', msg='')

@route('/login', method='POST') 
def do_login():
    timer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_ip = request.environ.get('REMOTE_ADDR')
    #print(dictUser)
    username = request.forms.get('username')
    password = request.forms.get('password')
    
    db = sqlite3.connect('transPlus.db')
    c = db.cursor()
    c.execute("SELECT * FROM account")
    data = c.fetchall()
    c.close()
    for x in data:
        dictUser[x[1]] = x[2]
    #print(dictUser)
    
    if username in dictUser:
        #if dictUser[username] == password and client_ip=='127.0.0.1': #block ip state
        if dictUser[username] == password: #normal state
            s = request.environ.get('beaker.session')  
            s['user'] = username
            s['password'] = password
            s.save()
            dictUser.clear()
            
            print("Time: {}, IP: {}".format(timer, client_ip))
            return redirect('/')
        else:
            return template('views/login', msg='Sorry, your account or password is wrong!')
    else:
        return template('views/login', msg='Sorry, your account or password is wrong!')
    

def checkLogin():
    s = request.environ.get('beaker.session') 
    username = s.get('user',None)
    if username != None:
        return True
    else:
        return False
    
@route('/logout')   
def logout():
    response.set_cookie('user','') 
    s = request.environ.get('beaker.session')  
    s['user'] = None
    s['passwoed'] = None
    s.save()    
    return template('logout')
    
@route('/questboard')
def showQuestboard():
    if checkLogin():
        db = sqlite3.connect('transPlus.db')
        c = db.cursor()
        c.execute("SELECT * FROM quest")
        data = c.fetchall()
        #print(data)
        c.close()
        output = template('views/questboard', rows=data, title="Menu System")
        return output
        
    else:
        return template('views/loginMsg')
    
@route('/process', method='POST')
def do_process():
    dateAndTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    qId = request.forms.get('qId')
    db = sqlite3.connect('transPlus.db')
    c = db.cursor()
    c.execute("UPDATE quest SET process = :process, processTime = :processTime WHERE id = :qId",{"qId":qId, "process": 'TRUE', "processTime":dateAndTime})
    db.commit()
    c.close()
    return redirect('/questboard')
      

#this is get the android msg method
@route('/quest/<QuestString>')
def Questionnaire(QuestString):
    dateAndTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    li = QuestString.split("&")
    qType = li[0]
    qWord = li[1]
    qMsg = li[2]
    db = sqlite3.connect('transPlus.db')
    c = db.cursor()
    #insert statement
    c.execute("INSERT INTO quest (type, word, message,time, process) VALUES (?,?,?,?,'FALSE')", (qType, qWord, qMsg, dateAndTime))
    db.commit()
    c.close()
    return template('<h1>This is our getting messaage</h1><b>Tpye: </b>{{Type}}<br><b>Message: </b>{{msg}}<h2>Uploaded to database!</h2>',Type= qType,msg=qMsg)

@route('/questCollect/<QuestString>')
def QuestCollect(QuestString):
    li = QuestString.split("&")
    return template('<h1>This is we getting messaage</h1>{{row}}',row = li)

@route('/terminology')
def showTerminology():
    if checkLogin():
        db = sqlite3.connect('transPlus.db')
        c = db.cursor()
        c.execute("SELECT * FROM terminology")
        data = c.fetchall()
        c.execute("SELECT * FROM modifyTime WHERE page='terminology'")
        time = c.fetchone()
        c.close()
        output = template('views/terminologyboard', rows=data, title="Terminology", time=time[1])
        return output
        
    else:
        return template('views/loginMsg')
    
@route('/terminologyTest')
def showTerminologyTest():
    if checkLogin():
        db = sqlite3.connect('transPlus.db')
        c = db.cursor()
        c.execute("SELECT * FROM terminology")
        data = c.fetchall()
        c.execute("SELECT * FROM modifyTime WHERE page='terminology'")
        time = c.fetchone()
        c.close()
        output = template('views/testTerminologyboard', rows=data, title="Terminology", time=time[1], searchName="ウインナー")
        return output
        
    else:
        return template('views/loginMsg')
    
@route('/terminology/add')
def addForm():    
    if checkLogin():
        return template('addTerminology')
    else:
        return template('views/loginMsg')
@route('/terminology/add', method="POST")
def addTerminology():  
    dateAndTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pwd = request.forms.get("confirmPwd")
    generate = request.forms.getlist('checkGenerate')[0]
    #print(generate, type(generate))
    ja = request.forms.getunicode('ja')
    zh = request.forms.getunicode('zh')
    s = request.environ.get('beaker.session')
    if pwd == s['password'] and ja!="" and zh!="":
        db = sqlite3.connect('transPlus.db')
        c = db.cursor()
        #insert statement
        c.execute("INSERT INTO terminology (ja, zh) VALUES (?,?)", (ja,zh))
        c.execute("UPDATE modifyTime SET time = :time WHERE page = 'terminology'",{"time":dateAndTime})
        db.commit()
        c.close()
        if generate == "True":
            listDir = os.listdir('./simple_images')
            if ja not in listDir: # check the file in dir
                downloadImage(ja)
        return redirect('/terminology')
    else:
        return '<h1>error</h1>'

@route('/terminology', method='POST')
def modifyTerm():
    #dateAndTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print(dateAndTime)
    TermId = request.forms.get('id')
    ja = request.forms.getunicode('ja')
    zh = request.forms.getunicode('zh')
    #print(dictUser)
    return template('terminologyform' , termId = TermId, jaName = ja , zh=zh)

@route('/modify', method='POST')
def sendTerm():
    dateAndTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print(dateAndTime)
    pwd = request.forms.get("confirmPwd")
    termId = request.forms.get("wordId")
    term = request.forms.getunicode("newTerm")
    s = request.environ.get('beaker.session')
    if pwd == s['password'] and term!="":
        db = sqlite3.connect('transPlus.db')
        c = db.cursor()
        c.execute("UPDATE terminology SET zh = :term WHERE id = :id",{"term":term, "id":termId})
        c.execute("UPDATE modifyTime SET time = :time WHERE page = 'terminology'",{"time":dateAndTime})
        db.commit()
        c.close()
        return redirect('/terminology')
    else:
        return '''<h1>wrong password</h1>'''
    
@route('/imageFolder')
def showImageFile():
    if checkLogin():
        db = sqlite3.connect('transPlus.db')
        c = db.cursor()
        c.execute("SELECT * FROM modifyTime WHERE page='imageFolder'")
        time = c.fetchone()
        c.close()
        listDir = os.listdir('./simple_images')
        output = template('views/Imageboard', rows=listDir, title="Image", time=time[1])
        return output
        
    else:
        return template('views/loginMsg')
    
@route('/imageFolder/<filename>')
def showImage(filename):
    if checkLogin():
        output = template('views/imageForm', filename=filename)
        return output
    else:
        return template('views/loginMsg')
    
@route('/imageFolder/<filename>', method='POST')
def do_upload(filename):
    pwd = request.forms.get("confirmPwd")
    dateAndTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    upload = request.files.get('upload')
    s = request.environ.get('beaker.session')
    if pwd == s['password'] and upload!="":
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png', '.jpg', '.jpeg'):
            return "File extension not allowed."
    
        save_path = "./simple_images/{category}".format(category=filename[:-4])
        if not os.path.exists(save_path):
            os.makedirs(save_path)
    
        file_path = "{path}/{file}".format(path=save_path, file=filename)
        #print(file_path)
        upload.save(file_path, overwrite=True)
        resizeImgFunc(filename,file_path)
        
        db = sqlite3.connect('transPlus.db')
        c = db.cursor()
        c.execute("UPDATE modifyTime SET time = :time WHERE page = 'imageFolder'",{"time":dateAndTime})
        db.commit()
        c.close()
        return redirect('/imageFolder/{}'.format(filename))
    else:
        return "<h1>Failed</h1><a href='/imageFolder/{}'>link</a>".format(filename)
        
if __name__ == "__main__":
    app = default_app()
    app = SessionMiddleware(app, session_opts)
    run(app=app, host='0.0.0.0', port=8080, debug=True, reloader=True)