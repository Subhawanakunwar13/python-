class Bank:
    def _init_(self,name,balance):
        self._name=name
        self.__balance=balance

        @property
        def getbalance(self):
            return self._balance
        
        @getbalance.setter
        def setbalance(self,balance):
            self.__balance=balance

            
            
        def calculatemunbalance(self):
                return self.__balance>500
user1=Bank("sub",1000)
print(user1._name)
print(user1.getbalance)
user1.setbalance=2000
print(user1.getbalance)



#abstrction method
from abc import ABC,abstractmethod
class Coffee(ABC):
     def makeCoffee(self):
          self.gason()
          self.addCoffee()
          self.addMetrial()
          self.serveon()
class Espresso(Coffee):
    @abstractmethod
     def gason(self):
          print("coffee machine on")
          
     @abstractmethod
    def addCoffee(self):
          print("addCoffee beans")
          
     @abstractmethod
     def addMetrial(self):
         print("water,suger,milk")
        
     @abstractmethod
     def serveon(self):
          print("serve in cup")
          
class Cappuccino(Coffee):
    def gason(self):
        print("coffee machine on")
    def addCoffee(self):
        print("extracted coffee powder")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")

exp = Espresso()
exp.makeCoffee()

cap = Cappuccino()
cap.makeCoffee()