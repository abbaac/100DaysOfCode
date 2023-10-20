# Write your code below this line 👇

def prime_checker(number):
  prime = True
  for i in range(1,number+1):
    if (i != 1) and (i != number):
      if number % i == 0:
        prime = False
        break
  if prime == False:
    print("It's not a prime number.")
  elif prime == True:
    print("It's a prime number.")
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = 87 # Check this number
prime_checker(number=n)