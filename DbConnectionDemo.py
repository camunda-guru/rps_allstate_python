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
#SELECT p.PolicyNo,c.CustomerName,p.MaturityAmount
#  FROM dbo.Policy p, dbo.Customer c where p.PolicyNo=c.PolicyNo;

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

def getPolicies():
    connObj = createConnection()
    cursor = connObj.cursor()
    cursor.execute("select * from Policy")
    return cursor.fetchall()
      
def fetchByPolicyId(id):
    conn = createConnection()
    cursor = conn.cursor()
    cursor.execute("""select * from Policy where 
    PolicyNo='%d'""" % (id))
    return cursor.fetchall()

def fetchByPolicyandCustomerById():
    conn = createConnection()
    cursor = conn.cursor()
    cursor.execute("""SELECT p.PolicyNo,c.CustomerName,p.MaturityAmount
  FROM Policy p, Customer c where 
     p.PolicyNo=c.PolicyNo""" )
    return cursor.fetchall()

#testData=[4222,2453453,4274];
#addPolicy(testData); 
#Retrieve Data
for row in fetchByPolicyandCustomerById():
    print(row)
       
        