# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:26:00 2021

@author: arman
"""

import sqlite3


db = sqlite3.connect('trans.db')
db.execute("DROP TABLE quest")
db.execute("CREATE TABLE quest (id INTEGER PRIMARY KEY, ja CHAR(255) NOT NULL, zh CHAR(255) NOT NULL)")
db.execute("INSERT INTO quest (ja,zh) VALUES ('111','aa')")
db.execute("INSERT INTO quest (ja,zh) VALUES ('222','aabb')")
db.execute("INSERT INTO quest (ja,zh) VALUES ('331','acca')")
db.execute("INSERT INTO quest (ja,zh) VALUES ('444','addda')")
db.execute("INSERT INTO quest (ja,zh) VALUES ('555','eeaea')")
db.execute("delete from quest where id=2")


db.commit()



db = sqlite3.connect('trans.db')
db.execute("DROP TABLE quest_back")
db.execute("CREATE TABLE quest_back (id INTEGER PRIMARY KEY, ja CHAR(255) NOT NULL, zh CHAR(255) NOT NULL)")
c = db.cursor()
c.execute("SELECT * FROM quest")
data = c.fetchall()
for x in data:
    db.execute("INSERT INTO quest_back (ja,zh) VALUES (?,?)",(x[1],x[2]))
c = db.cursor()


c.execute("SELECT * FROM quest_back")
data = c.fetchall()
print(data)

c.close()