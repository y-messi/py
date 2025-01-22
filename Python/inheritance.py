# single inheritance

class Parent:
    def display(self):
        print("Parent")
        
class child(Parent):
    def show(self):
        print("child")
        
x=Parent()
x1=child()
x.display()
x1.display()
x1.show()
        
# multi level inheritance

class gp:
    def gdisplay(self):
        print("grand parent")
        
class p(gp):
    def pdisplay(self):
        print("parent")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
class c(p):
    def cdisplay(self):
        print("child")
        
c1 = c()
c1.gdisplay()
c1.pdisplay()   
c1.cdisplay() 




# hierachical inheritance

class Parent1:
    def p1display(self):
        print("my parent")
        
class child1(Parent1):
    def c1display(self):
        print("child1")
        
class child2(Parent1):
    def c2display(self):
        print("child2")
        
c = Parent1()  
c.p1display()      
c1 = child1()
c2 = child2()
c1.c1display()
c1.p1display()
c2.c2display() 
c2.p1display()




# multiple inheritance

class Father():
    def fdisplay(self):
        print("this is our father")
        
class Mother():
    def mdisplay(self):
        print("this is our mother")
        
class Child(Father, Mother):
    def ccdisplay(self):
        print("this is our child")
        
        
c10 = Child()
c10.ccdisplay()  
c10.mdisplay()
c10.fdisplay()              
                              
                    
              