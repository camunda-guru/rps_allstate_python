# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:38:53 2018

@author: Balasubramaniam
"""

import os
import datetime
import random
path="F:\AllState_Python2018\logs"

subdirName=input("Enter Sub Directory Name")
fileName="File"+datetime.datetime.now().strftime("%H-%M-%S")+".log"
print(fileName)

if(os.path.exists(path)):
   status=True
else:
      
    dirRef=os.mkdir(path,mode=0o777)
    status=True
    
if(status):
    os.mkdir(path+"\\"+subdirName,mode=0o777)
    fileRef=open(path+"\\"+subdirName+"\\"+fileName,"a")
    for _ in range(1,100):
        fileRef.write(str(random.randint(100,10000)))
        
    fileRef.close()    

   
        
        
        
        