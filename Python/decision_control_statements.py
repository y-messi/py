# if statement

n = int(input("Enter the value n "))
if(n==0):
    print("ZERO" )
    
    
# if else statement

a = int(input("Enter the value of a "))
if(n>0):
    print("POSITIVE")
    
else:
    print("NEGATIVE")   
    
    
#nested if

x = int(input("Enter the value of x "))
y = int(input("Enter the value of y ")) 
z = int(input("Enter the value of z "))
if(x>y):
    if(a>z):
        print("x is large")
    else:
        print("c is large")
        
elif(y>z):
    print("y is large")
    
else:
    print("c is large") 
    
    
# if-elif-else

m = int(input("Enter the value of m = ")) 
n = int(input("Enter the value of n = "))
if(m==n):
    print("Both are equal")
    
elif(m>n):
    print("m is greaterthan n")
    
else:
    print("n is lessthan m")                                     