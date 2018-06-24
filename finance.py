'''
Created on 02-Jun-2016

@author: BALASUBRAMANIAM
'''
def addTax(price, tax):
        newPrice = price / 100 * (100 + tax)
        return newPrice
    


def calculateDiscount(price, discount):
        newPrice = price-discount
        return newPrice
    
if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")