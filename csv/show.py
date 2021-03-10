# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 11:41:52 2021

@author: arman
"""

import sqlite3

db = sqlite3.connect('../transPlus.db')
c = db.cursor()
c.execute("SELECT * FROM terminology")
data = c.fetchall()
print(data)
c.close()