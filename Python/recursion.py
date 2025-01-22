#factorial
n = int(input("Enter n value "))
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
res = factorial(n)
print("The factorial of ", n, "is", res)     