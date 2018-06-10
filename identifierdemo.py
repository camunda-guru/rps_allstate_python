# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 09:47:09 2018

@author: Balasubramaniam
"""

"""
#print statement
print("Welcome to Python Coding...")
#identifiers
firstName="Sandeep"
lastName="Sharma"
#reading input from user
address=input("Enter Address")
#parameters
print("First Name=%s\nLast Name=%s" %(firstName,lastName))
print("Address=%s" %(address))
#check the type
print(type(firstName))
#read age
age=int(input("Enter Age"))
print(type(age))
print("Age=%d" %(age))
"""
#conversions
#int in hex
memoryAddress=255
hexMemoryAddress=hex(memoryAddress)
print(hexMemoryAddress)
print("Memory Address in hex=%X" %(memoryAddress))

#binary to int conversion
print(int('100010',2))
#integer to binary
print(bin(45))
#octal conversion
print(oct(65))
#complex number
real=67
imaginary=87
print(complex(real,imaginary))

from datetime import date
print(date.today())

















