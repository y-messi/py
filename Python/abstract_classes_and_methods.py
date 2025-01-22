# abstract classes - classes which contain / have abstract methods
# abstract methods - methods with declaration but not definition
# concrete class - class without abstract methods
# objects cannot be created for abstrat class
# objects can only be created for concrete classes
# :- we have to change from abstract to concrete class

from abc import ABC,abstractmethod

class Aclass(ABC):
    @abstractmethod
    def display(self):
        None
        
class Demo(Aclass):
    def display(self):
        print("Abstract Methods")  
        
c1 = Demo()
c1.display()              

