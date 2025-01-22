import random


a=10
b=15


#random()-float value btn 0.0 to 1.0
print(random.random())

#uniform()- float values btn a and b
print(random.uniform(a, b))

#randint(a,b)- integer value btn a and b
print(random.randint(a,b))

#getrandbits(k)- integer value in btn the min and max decimal values from a given bit k
print(random.getrandbits(b)) 
print(random.getrandbits(a)) 


#choice(seq)- element from a given sequence elements
z=[1,2,3,4,5,6,7,8,9]
print(random.choice(z)) 