a = [1,2,3,4,5]
b = [1,2,3,1,4,1,5]

#built-in functions/methods (return value bt doesnot change the list)
#count()
print(a.count(4))
print(b.count(1))

#index()
print(a.index(4))
print(b.index(1))

#index(value, starting index)
print(a.index(4,2))
print(b.index(5,1))

#Doesnot return value but cahnges the list
#append()
x = [1,2,3,4,5]
y = [1,2,3,1,4,1,5]
print(x.append(7))
print(x.extend([6,7,8]))
print(x.insert(0,10))
print(x.remove(4))
print(x.reverse())
print(y.sort())
print(x.pop())