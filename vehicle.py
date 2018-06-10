# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:45:06 2018

@author: Balasubramaniam
"""

class Vehicle:
    def __init__(self,regNo,engineNo,color):
        self.__regNo=regNo
        self.__engineNo=engineNo
        self.__color=color
        
    def setPolicyHolder(self,obj):
        self.__policyHolderObj=obj
    def setDriver(self,obj):
        self.__driverObj=obj
    
    def getRegNo(self):
        return self.__regNo
    def getEngineNo(self):
        return self.__engineNo
    def getColor(self):
        return self.__color
  
    def getPolicyHolder(self):
        return self.__policyHolderObj
    
    def getDriver(self):
        return self.__driverObj