# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:26:00 2021

@author: arman
"""

import sqlite3
db = sqlite3.connect('transPlus.db')
db.execute("DROP TABLE account")
db.execute("CREATE TABLE account (id INTEGER PRIMARY KEY, username CHAR(16) NOT NULL, password CHAR(16) NOT NULL)")
db.execute("INSERT INTO account (username, password) VALUES ('admin', 'admin')")
db.execute("INSERT INTO account (username, password) VALUES ('arman', '0420')")
db.commit()


db = sqlite3.connect('transPlus.db')
db.execute("DROP TABLE quest")
db.execute("CREATE TABLE quest (id INTEGER PRIMARY KEY, type CHAR(16) NOT NULL, word CHAR(255) NOT NULL, message CHAR(255) NOT NULL, time CHAR(255) NOT NULL, process CHAR(5) NOT NULL, processTime CHAR(255))")
db.execute("INSERT INTO quest (type, word, message,time,process) VALUES ('Test', 'おでん', 'This is test','2021-03-07 14:24:32' ,'FALSE')")
db.commit()

db = sqlite3.connect('transPlus.db')
db.execute("DROP TABLE modifyTime")
db.execute("CREATE TABLE modifyTime (page CHAR(255) NOT NULL PRIMARY KEY, time CHAR(255) NOT NULL)")
db.execute("INSERT INTO modifyTime (page, time) VALUES ('terminology','2021-03-07 13:33:29')")
db.execute("INSERT INTO modifyTime (page, time) VALUES ('imageFolder','2021-03-08 18:00:17')")
db.commit()