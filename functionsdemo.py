# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:40:08 2018

@author: Balasubramaniam
"""

#claim settlement
import datetime;
def claimsettlement(amount):
    status = ""
    currentTime = datetime.datetime.now().hour;
    if (amount < 500):       
        if (currentTime > 15):
            status = "Fund Transfer will happen in next working day"
        else:
            status = "Fund Transfer initiated"

    else:
        status("Invoke Assessment Process")

    return status
        
        





