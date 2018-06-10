# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 09:35:56 2018

@author: Balasubramaniam
"""
from policy_holder import PolicyHolder
from driver import Driver
from vehicle import Vehicle
import datetime
#create object
fromDate = datetime.date(2015,1, 1)  #year, month, day
toDate=datetime.date(2019,1,1)
dob=datetime.date(1978,4,21)

vehicleObj=Vehicle("TN-02-4556",43876587435,"Red")
vehicleObj.setPolicyHolder(PolicyHolder(237467,fromDate,toDate,"Sanjay","Male",dob))
vehicleObj.setDriver(Driver(429654,"Kiran"))

print(vehicleObj.getPolicyHolder().getName(),"--->",vehicleObj.getRegNo())

