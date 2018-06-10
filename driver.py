# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:50:53 2018

@author: Balasubramaniam
"""

class Driver:
    def __init__(self,licenseNo,name):
        self.__licenseNo=licenseNo
        self.__name=name
        
    def setAddress(self,addr):
        self.__address=addr        
  
    def setPhoneNo(self,phone):
        self.__phoneNo=phone
        
    def getAddress(self):
        return self.__address
           
    def getPhoneNo(self):
        return self.__phoneNo