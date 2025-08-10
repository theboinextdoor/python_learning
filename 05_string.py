str1 = "I am a Coder "
str2 = "I am an Open Source Contributer"
print(str1)
print(str2)
# length 
len_of_str1= len(str1)
len_of_str2= len(str2)

print("Length of total string: ",len_of_str1+len_of_str2)
print(str1[0:6])
print(str1.capitalize())       #Capitalize method
print(str2.endswith("af"))     #endswith method
print(str1.replace("Coder", "Programmer"))
print(str1.find("Coder"))

str3 = "Faraaz , Aiman , Faiz, Fatima , "
print(str3.strip().split(","))

age = 24
txt = f"My age is {age}"
print(txt)

name = "Faraaz"
print(name.swapcase())