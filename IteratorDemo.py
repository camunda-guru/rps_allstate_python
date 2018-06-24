'''
Created on 27-Jun-2017

@author: BALASUBRAMANIAM
'''

class ReadData(object):
    def __init__(self,min,max):
        self.min=min
        self.max=max
    def __iter__(self):
        return(self)
    def __next__(self):
        if(self.min>self.max):
            raise StopIteration('Exceeded the limit')
        else:
            self.min+=5
            return self.min-5
        
readData=ReadData(50,100)
print(next(readData))
iterableData = iter(readData)
while True:
    try:
       print(iterableData.__next__(),end='') 
    except StopIteration as e:
       print() 
       print(e) 
       break
           

            
         