'''
Created on 26-Jun-2017

@author: BALASUBRAMANIAM
'''
from xml.dom import minidom

doc = minidom.parse("RouterInformation.xml")

routers=doc.getElementsByTagName("Router")

for router in routers:
    print(router.getElementsByTagName("HostName")[0].firstChild.data)
    interfaceData=router.getElementsByTagName("Interfaces")
    for interface in interfaceData:
        print(interface.getElementsByTagName("InterfaceNo")[0].firstChild.data)
    
    
    
    
    
    
