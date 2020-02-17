# euler problem 1

sum = 0
for i in range(1000):
    if (i%3==0 or i%5==0):
        sum = sum + 1
    
print ("the sum of all multiples of 3 or 5 is equal to" , sum)



# euler problem 3 
def PrimeFactorLarge(x):
    prime = 1
    b = 2
    
    while b <= x/b:
        if x % b == 0:
            prime = b 
            x /= b 
        else:
            b +=1
            
    if prime < x:
        prime = x 	

    return prime

print(PrimeFactorLarge(600851475143))
		    

#Problem 4 by Adam
def largest_palindrome():
  palin = 0

  for x in range(999, 100, -1):
      for y in range(x, 100, -1):
         product = x * y

         if product > palin:
            palin_string = str(product)
            if palin_string == palin_string[::-1]:
                palin = product
  return palin

print(largest_palindrome())
