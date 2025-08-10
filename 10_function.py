
# #! Function: In Python a function is defined using the def keyword:
# def printStatement():
#   print("Hello my name is Faraaz")

# printStatement()

# #TODO: Argument in Function
# #! Information can be passed into functions as arguments.
# #! Arguments are specified after the function name, inside the parentheses.
# #! You can add as many arguments as you want, just separate them with a comma.

# def myFuncArgg(f_name):
#   print(f_name +" "+ "Ashraf")

# myFuncArgg("Faraaz")
# myFuncArgg("Aiman")
# myFuncArgg("Zoya")
# myFuncArgg("Asad")

# #TODO: Default Parameter in Function
# def myfuncPara(name = "Faraaz"):
#   print("My Name is ", name)

# myfuncPara()
# myfuncPara("Aiman")

# #TODO: Keyword Arguments
# #! You can also send arguments with the key = value syntax.
# #! This way the order of the arguments does not matter.

# #! Example: 
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# #TODO:  Arbitrary Arguments, *args
# #! If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# # def myFunc():
# #   print()


# #TODO: Passing a List as an Argument

# def myfruitFunc(fruits):
#   for x in fruits:
#     print(x)

# fruits = ["Apple", "Mango", "Guava"]
# myfruitFunc(fruits)


# #TODO: Recursion:
def show(n):
  if(n == 0):
    return
  print(n)
  show(n-1)

show(12)