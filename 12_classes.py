# class Account:
#   def __init__(self, bal, acc):
#     self.balance = bal
#     self.account_no = acc

#   def debit(self, amount):
#     self.balance -=amount
#     print("Rs", amount ,"was debited from your Account no: ", self.account_no)
#     print("Total Balance = ", self.getbalance())

#   def credit(self, amount):
#     self.balance +=amount
#     print("Rs", amount ,"was credited to your Account no: ", self.account_no)
#     print("Total Balance = ", self.getbalance())
  
#   def getbalance(self):
#     return self.balance

# acc1= Account(10000, 337175500770)
# acc1.debit(1000)
# acc1.credit(500)


#! Abstraction
class Person:
  def __init__(self, name):
    self.__name = name

  def __hellow(self):
    print("hellow", self.__name)

  def welcome(self):
    self.__hellow()

p1 = Person("Farazz")
p1.welcome()