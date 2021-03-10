# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:24:41 2021

@author: arman
"""
import csv
import sqlite3

def downloadCSV():
    #get data in database
    db = sqlite3.connect('transPlus.db')
    c = db.cursor()
    c.execute("SELECT * FROM terminology")
    data = c.fetchall()
    c.close()
    #print(data)
    
    with open('./static/csv/terminology.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
    
        writer.writerow(['ja','zh-tw'])
        for row in data:
            writer.writerow([row[1], row[2]])
    return True      
          
if __name__ == "__main__":
    print(downloadCSV())