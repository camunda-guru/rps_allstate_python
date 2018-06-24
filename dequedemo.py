'''
Created on 27-Jun-2017

@author: BALASUBRAMANIAM
'''
from collections import deque
import random
dataQueue=deque()

for i in range(100):  
  dataQueue.append(random.randint(1,200))
dataQueue.appendleft('items')

print(dataQueue)
