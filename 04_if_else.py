# age = int(input("what is your age: "))
# if(age < 18):
#   print("You are under age...")
# elif(age > 90):
#   print("You are above age...")
# else:
#   print("You are good to go.....")


# food = input("food :")
# eat = "Yes" if food == "cake" else "no"
# print(eat)

# food= input("food: ")
# print("sweet") if food == 'cake' or food == "jalebi" else print("not sweet")


age = int(input("Age: "))
vote = ("yes" , "no") [age < 18]
print(vote)
