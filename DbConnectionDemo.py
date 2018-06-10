# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:40:25 2018

@author: Balasubramaniam
"""

import pyodbc

def createConnection():
    conn =  pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=DESKTOP-55AGI0I\SQLEXPRESS;DATABASE=AllStateDB;'
                      'UID=sa;PWD=vignesh')
    return conn;


def addPolicy(data):
    connObj = createConnection();
    cursor = connObj.cursor();
    print("Cursor ready...");
    try:
        cursor.execute("""insert into Policy values 
    ('%d','%d','%d')""" % (data[0], data[1],data[2]));
        # cursor.execute(query);
        connObj.commit()
    except pyodbc.Error as e:
        print("Exception occurred", e)
        connObj.rollback()
        

testData=[4222,2453453,4274];
addPolicy(testData);        
        