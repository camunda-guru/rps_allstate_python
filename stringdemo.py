# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:26:18 2018

@author: Balasubramaniam
"""

orgName="All State Corporation Limited"
#slicing
print(orgName[5:8])
print(orgName[:-5])
print(orgName[2:])
city="new delhi"
print(city.capitalize())
#padding
country="India"
print(country.center(len(country)+40,"*"))
#rpad
amount=3284582
stramount=str(amount)
print(stramount.rjust(len(stramount)+10,"*"))
#reverse string
print(country[::-1])
#encoding and decoding
seqNo=567
print(type(seqNo))
import base64
pnrNo=base64.b64encode(str(seqNo).encode(encoding='utf-8',
                       errors='strict'))
#for loop
for _ in pnrNo[0:]:
    print(chr(int(_)),end="")
    
#decoding
originalData=base64.b64decode(pnrNo.decode(encoding='utf-8',
                       errors='strict'));
print("\n");                                           
for _ in originalData[0:]:
    print(chr(int(_)),end="");














