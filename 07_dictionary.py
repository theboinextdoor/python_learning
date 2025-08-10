# Dictionaries are used to store data values in key:value pairs.A  dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# dict = {
#   "name" : "faraz",
#   "age" : 24,
#   "subject" : ["Python", "Web Development" , "Android Development"],
#   "background-color" : (255, 255, 255 , 255),
#   "is_adult" : True,
# }
# print(dict)


# # TODO : Access Items: 
# print(dict["age"])
# print(dict.get("is_adult"))
# print(dict.keys())
# print(dict.values())


# # TODO : Change the Value
# # dict["name"] = "Aiman"
# # print(dict)

# print(dict.values())


# # TODO : Nested Dictionary:
# dict2 = {
#   "name" : "Faraaz",
#   "age" : 24,
#   "friend" : {
#     "name": "Anonymous",
#     "age" : 23,
#     "profssion": "Doctor",
   
#     "isActive" : False
#   },
#   "isActive":True 
# }
# print("Dictionary 2: ", dict2)
# print(dict2["friend"]["profssion"])

# # TODO: Update the values:
# dict2.update({"isActive": False}) 
# if "friend" in dict2 and "name" in dict2["friend"] :
#   dict2["friend"]["name"]= "Anonymous Person"

# # TODO: Adding the item:
# dict2["salary"]= 50000
# dict2["friend"]["salary"]=60000
# print(dict2)

# # TODO: Remove items
# dict2.pop("friend")
# print(dict2)

# dict2.popitem()   #! Removes the last item
# print(dict2)

# del dict2["isActive"]
# print(dict2)
# dict2.clear()
# print(dict2)

# # TODO : Looping in dictionary:
# dict2 = {
#   "name" : "Faraaz",
#   "age" : 24,
#   "friend" : {
#     "name": "Anonymous",
#     "age" : 23,
#     "profssion": "Doctor",
   
#     "isActive" : False
#   },
#   "isActive":True 
# }

# for x in dict2:        #! it return the Key
#   print(x)

# print("Returning the Value: ")
# for x in dict2 :      #! it returns the value
#   print(dict2[x])

# for x in dict.values():
#   print(x)

# for x , y in dict2.items():
#   print(x , y)

# TODO: Copy Dictionary: 
dict2 = {
  "name" : "Faraaz",
  "age" : 24,
  "friend" : {
    "name": "Anonymous",
    "age" : 23,
    "profssion": "Doctor",
   
    "isActive" : False
  },
  "isActive":True 
}

# otherDict = dict(dict2)
otherDict = dict2.copy()
# print(otherDict)

# TODO : Looping in Nested Dictinary:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

