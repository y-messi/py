#sets

s={1,2,3,4}
t={3,4,5,6,7}

print(s)
print(t)

print(len(s))
print(len(t))

s.add(5)
t.add(8)
print(s)
print(t)

s.update(t)
print(s)
t.update(s)
print(t)

s.remove(5)
print(s)
t.remove(8)
print(t)

s.discard(7)
print(s)


print(s.pop())

s.clear()
print(s)

x={1,2,3}
y={4,5,6}
print(max(x))
print(max(y))

print(min(x))
print(min(y))

print(sum(x))
print(sum(y))


a={1,2,3}
b={1,2,3,4,5,6}

print(a.issubset(b))
print(b<=a)

print(a.issuperset(b))
print(b>=a)

print(a.union(b))
# a!b

print(a.intersection(b))
# a&b

#difference
print(a.difference(b))
#a-b
print(b.difference(a))
#b-a

#symmetric difference
m={1,2,3,7,8,9}
n={1,2,3,4,5,6}
print(m.symmetric_difference(n))
#s^t
