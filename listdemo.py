# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:20:37 2018

@author: Balasubramaniam
"""

import random

#print(random.randint(5,10))
#generate 100 customerids
#create the list
customerIdList=[]
for _ in range(1,5):
    customerIdList.append(random.randint(10000,100000))
print("Before Sorting....")    
print(customerIdList)    
customerIdList.sort()  
print("After Sorting....")      
print(customerIdList)
customerIdList.reverse()
print("After Sorting in Reverse....")      
print(customerIdList)
"""
#heterogenous data
machineInfo=["172.89.90.91",8080,"PC-1",True,6060,"Port occupied",7070]
for _ in machineInfo:
    #print(type(_))
    if (type(_) is str) :
       print("String %s" %(_))
       print("Done...")
    elif(type(_) is int):
        print(_+100)
    else:
        print(_)
#to remove duplicates
data=[4,5,5,6,7,7]
print(set(data))       
"""       
policy=["Policy1","Policy2","Policy3"]
years=[4,5,8]
sumInsured=[261546,1856822,2010712]
#finalList=policy+years+sumInsured
#print(finalList)
for (x,y,z) in zip(policy,years,sumInsured):
    print(x,y,z)
#list of list
customerList=[[1,"Ajay",3264567],[2,"Seema",674567],[3,"Shyam",3786567]]
for outer in customerList:
    for inner in outer:
        if(type(inner) is str):
            print(inner)
    






















    
    
