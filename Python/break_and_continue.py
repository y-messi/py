#Also uses iterative control statements ie for and while

#while loop with break statement
i = 1
while(i<=10):
    print(i)
    if(i==5):
        break
    i=i+1
    
print("LOOP TERMINATES")    

#for loop with continue statement
for i in range(1,10):
    if(i==5):
        continue
    print(i)
    
print("loop terminates")    