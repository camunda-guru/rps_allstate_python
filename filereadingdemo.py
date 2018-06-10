# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:18:20 2018

@author: Balasubramaniam
"""

import os
path="F:\AllState_Python2018"

for (dirpath,dirnames,filenames) in os.walk(path):
    #print(filenames)
    #print(dirnames)
    for file in filenames:
        #print(file)
        (filename,extension)=os.path.splitext(file)
        #print(filename,"-->",extension) 
        if(extension == ".csv"):
            content=open(path+"\\"+file,'r')
            for line in content:
               print(line)
            
            
            
            
            