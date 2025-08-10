class Car:
  
  @staticmethod
  def start():
    print("Car Started....")

  @staticmethod
  def stop():
    print("Car Stoped....")

class ToyotaCar(Car):
  def __init__(self , name):
    self.name= name

car1 = ToyotaCar("Fortuner")
car1.start()
car1.stop()