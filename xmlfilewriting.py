# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:16:55 2018

@author: Balasubramaniam
"""

from xml.dom import minidom
#create DOM object
doc=minidom.Document()
#rootnode
rootElement=doc.createElement("Claims")
doc.appendChild(rootElement)
#claim
node=doc.createElement("Claim")
#node.setAttribute('ClaimId','12345')
rootElement.appendChild(node)
#claim id Node
childNode=doc.createElement("ClaimId")
textNode = doc.createTextNode('1234')
childNode.appendChild(textNode)
node.appendChild(childNode)

#PolicyNo Node
childNode=doc.createElement("PolicyNo")
textNode = doc.createTextNode('244354')
childNode.appendChild(textNode)
node.appendChild(childNode)

#Claim Amount
childNode=doc.createElement("ClaimAmount")
textNode = doc.createTextNode('58000')
childNode.appendChild(textNode)
node.appendChild(childNode)
#Status
childNode=doc.createElement("Status")
textNode = doc.createTextNode('In Progress')
childNode.appendChild(textNode)
node.appendChild(childNode)

#clement
childNode=doc.createElement("Clement")
textNode = doc.createTextNode('Raghu')
childNode.appendChild(textNode)
node.appendChild(childNode)
#indentation
xml_str = doc.toprettyxml(indent="  ")
with open("allstate_claims.xml", "w") as f:
    f.write(xml_str)

