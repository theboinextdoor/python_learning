
#! NOTE: 
#! Sets are used to store multiple items in a single variable.
#! Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

firstSet = {"Faraaz", "Amir" , "Arib" , "Raja"}
print(firstSet)           #! Note: the set list is unordered, meaning: the items will appear in a random order.


sets1= {"apple", "banana", "Guava", True, 1}
print(sets1)

#! Access the Element: 
for c in sets1 :
  print(c)
print("apple"in sets1)

#! Add the items
sets2 = {"faraaz", "aiman" , "aman", "anam"}
sets3 = {"karan", "arjun", "krish", "kapoor"}
sets2.update(sets3)
print(sets2)


#! Remove the Element:
sets3.remove('krish')
print(sets3)
sets3.discard('kapoor')
print(sets3)


#! Joint Method
#TODO:  union(), '|', intersectin(), difference(), symmetric_difference()
 
