# required args
def display(a,b):
    print("a = ", a, "b =" ,b)
    
display(10,20) 

# keyword args

def display(a,b):
    print("a=", a, "b=" ,b)
    
display(b=30,a=50) 

# default args

def display(name="abc", course="BIST"):
    print("name= ", name)
    print("course= ", course)
    
display(name="abc",course="CST")
display(name="PQR") 

# variable length args (*)

def display(* courses):
    for i in courses:
        print(i)
        
display("python", "java", "php", "ruby", "go", "react")        
   