# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:45:06 2018

@author: Balasubramaniam
"""

class Vehicle:
    #static variable 
    baseRoadTax=5000
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
    
    @staticmethod
    def computeTax(wheels):
        if (wheels==2):
            return Vehicle.baseRoadTax+2000
        if(wheels==4):
             return Vehicle.baseRoadTax+4000
         
    @classmethod
    def computeTaxByVehicle(cls,wheels):
        if ((wheels==2) and (cls.__name__=="HighEndVehicle")):
            return Vehicle.baseRoadTax+2000+Vehicle.baseRoadTax * .6
        if ((wheels==4) and (cls.__name__=="LowEndVehicle")):
             return Vehicle.baseRoadTax+4000++Vehicle.baseRoadTax * .4
         
            
#inheritance
class HighEndVehicle(Vehicle):
    
    def __init__(self,regNo,engineNo,color,airbrake,gps,autogear):
        Vehicle.__init__(self,regNo,engineNo,color) #invoke super class
        self.__abs=airbrake
        self.__gps=gps
        self.autogear=autogear
        
class LowEndVehicle(Vehicle):
    
    def __init__(self,regNo,engineNo,color,childLock):
        Vehicle.__init__(self,regNo,engineNo,color) #invoke super class
        self.__childLock=childLock
        
        
    
    