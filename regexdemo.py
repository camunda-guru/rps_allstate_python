# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 09:32:41 2018

@author: Balasubramaniam
"""
import re
re_pattern=r"[A-Z]{5,25}"

userName=input("Enter Name")

result=re.search(re_pattern,userName)
if(result):
    print("Match Found")
else:
    print("Match not found")