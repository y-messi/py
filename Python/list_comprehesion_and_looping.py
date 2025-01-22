list = [1,2,3,4,5,6]
print(list)

square = [i**2 for i in range(10)]
print(square)

square = [i**2 for i in range(4,10)]
print(square)

list = [10, 20, 30, 40, 50]
for i in list:
    print(i)
    
for i in range(10):
    print(i) 
    


odd = [1,3,5]
even = [2,4,6]
pair = [(x,y) for x in odd for y in even if x!=y]
print(pair)    