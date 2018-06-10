# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 09:33:49 2018

@author: Balasubramaniam
"""
import datetime
class PolicyHolder:
    
    def __init__(self,pno,fdate,tdate,name,gender,dob):
        self.__policyNo=pno
        self.__fromDate=fdate
        self.__toDate=tdate
        self.__policyHolderName=name
        self.__gender=gender
        self.__dob=dob
        
    def getPolicyNo(self):
        return self.__policyNo
    
    def getFromDate(self):
        return self.__fromDate
    
    def getToDate(self):
        return self.__toDate
    
    def getName(self):
        return self.__policyHolderName
    
    def getGender(self):
        return self.__gender
    
    def getDOB(self):
        return self.__dob
    
    def setAddress(self,addr):
        self.__address=addr
        
    def setEmailId(self,email):
        self.__emailId=email
        
    def setPhoneNo(self,phone):
        self.__phoneNo=phone
        
    def getAddress(self):
        return self.__address
        
    def getEmailId(self):
        return self.__emailId
    
    def getPhoneNo(self):
        return self.__phoneNo
    
        
#create object
fromDate = datetime.date(2015,1, 1)  #year, month, day
toDate=datetime.date(2019,1,1)
dob=datetime.date(1978,4,21)
obj=PolicyHolder(23747,fromDate,toDate,"Ajay","Male",dob)
obj.setAddress("Chennai")
obj.setPhoneNo(9952032852)
obj.setEmailId("param@gmail.com")

#access policyNo
print(obj.getName(),"->",obj.getPolicyNo(),"->",obj.getDOB().strftime("%A,%B,%Y"),obj.getAddress())



        
        
        
