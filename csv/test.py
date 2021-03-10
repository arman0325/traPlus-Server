# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 11:21:20 2021

@author: arman
"""
import csv 
import sqlite3

db = sqlite3.connect('../transPlus.db')
db.execute("DROP TABLE terminology")
db.execute("CREATE TABLE terminology (id INTEGER PRIMARY KEY, ja CHAR(255) NOT NULL, zh CHAR(255) NOT NULL)")
  
filename = "terminology.csv"
  
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r', encoding="utf-8") as csvfile: 
    csvreader = csv.reader(csvfile) 
      
    fields = next(csvreader) 
  
    for row in csvreader: 
        rows.append(row) 
  
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
print('Field names are:' + ', '.join(field for field in fields)) 
  
for row in rows: 
    print(row[0],row[1])
    db.execute("INSERT INTO terminology (ja, zh) VALUES (?, ?)", (row[0],row[1]))

db.commit()
print("complete")