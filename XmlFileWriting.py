'''
Created on 27-Jun-2017

@author: BALASUBRAMANIAM
'''
from xml.dom import minidom
#create DOM object
doc=minidom.Document()

rootElement=doc.createElement("Customers")
doc.appendChild(rootElement)
node=doc.createElement("Customer")
node.setAttribute('CustomerId','12345')
rootElement.appendChild(node)

accountNode=doc.createElement("Account")
node.appendChild(accountNode)

accountNo=doc.createElement("AccountNo")
text = doc.createTextNode('4334645')
accountNo.appendChild(text)
accountNode.appendChild(accountNo)

accountType=doc.createElement("Account_Type")
text=doc.createTextNode("Savings")
accountType.appendChild(text)

accountNode.appendChild(accountType)


xml_str = doc.toprettyxml(indent="  ")
with open("citrixcustomerdata.xml", "w") as f:
    f.write(xml_str)
