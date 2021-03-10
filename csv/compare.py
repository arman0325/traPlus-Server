# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 10:11:16 2021

@author: arman
"""
import csv 

  
filename = "new.csv"
filename2 = "terminology.csv"  
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r', encoding="utf-8") as csvfile: 
    csvreader = csv.reader(csvfile) 
      
    fields = next(csvreader) 
  
    for row in csvreader: 
        rows.append(row) 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
  
li = []
for row in rows: 
    li.append(row[1])
    

with open(filename2, 'r', encoding="utf-8") as csvfile: 
    csvreader = csv.reader(csvfile) 
      
    fields = next(csvreader) 
  
    for row in csvreader: 
        rows.append(row) 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
  
li2 = []
for row in rows: 
    li2.append(row[1])
    
for x in li2:
    if x not in li:
        print(x)
print("complete")