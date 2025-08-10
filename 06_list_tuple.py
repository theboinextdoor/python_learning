# !List : 

# list = [ 2,6,8,1,9,4,0]
# print(type(list))
# list.append(10)
# print(list)
# list.pop()
# print(list)
# list.sort()
# print(list)
# list.sort(reverse= True)
# print(list)
# list.remove(0)
# print(list)



#!Tuple : Tuples are used to store multiple items in a single variable.
# tup = (24 , 0 , 0)
# if 24 in tup :
#   print("yes 24 is present inside the Tuple...")
# else:
#   print("No, 24 is not present inside the Tuple...")


# !Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple" , "Kiwi" , "orange")
y = list(x)
y[1] = "Mango"
y.append("Grapes")
y.append("Guava")
x= tuple(y)
print(x)


# !Looping in Tuples : 
# for fruits in x:
#   print(fruits)

# for i in range(len(x)):
#   print(x[i])

i = 0
while i < len(x):
  print(x[i])
  i+=1