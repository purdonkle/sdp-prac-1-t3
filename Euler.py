# euler problem 1

sum = 0
for i in range(1000):
    if (i%3==0 or i%5==0):
        sum = sum + 1
    
print ("the sum of all multiples of 3 or 5 is equal to" , sum)