# implementing the same thing in different ways

# operator overloading
a = "hello"
b = "cads"
c = 30
d = 50
print(a +" "+ b)
print("c + d =" +" "+ str(c+d))

# method overloading

class Moverload():
    def display(self, x = None, y = None):
        print(x,y)
        
object = Moverload()
object.display() 
object.display(100)
object.display(200, 300)


# method overriding       
        
