# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:33:12 2018

@author: Balasubramaniam
"""
users=[{"id": 1,"name": "Leanne Graham","username": "Bret",
      "email": ["Sincere@april.biz","Leane@gmail.com"],
      "skillSet":["java","python","C"],
      },
    {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "skillSet":["java","python"],
    },
     {
    "id": 3,
    "name": "Clementine Bauch",
    "username": "Samantha",
    "email": "Nathan@yesenia.net",
    "skillSet":["java","C"],
    }

      ]

#print(user.keys())
#print(user.values())
#print(user["email"])
for user in users:
    for (key,value) in user.items():
        if(key == "name"):
          print(value,end="\t")
        if(key == "skillSet"):
            length=len(value)
            count=0
            for _ in value:
              if(count<length-1):  
                print(_,end=",")
                count=count+1
              else:
                print(_)





    