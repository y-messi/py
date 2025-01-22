#creating a class
class student:
    rno = 123
    name = "cads"
    branch = "Makerere"
    
    def read(self):
        print("Reading.......")
    def write(self):
        print("Writing.......")   
        
#accessing using an object        
cads = student()
print(cads.rno)
print(cads.name)
print(cads.branch) 

#accessing using function
cads.read()   
cads.write()    