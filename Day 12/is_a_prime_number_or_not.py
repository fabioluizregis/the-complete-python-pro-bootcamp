import math

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
       number_sqrt = int(math.sqrt(num))
       i=3
       while i <= number_sqrt:
           if num % i != 0:
               i += 2

           if num % i == 0:
               return False
       return True
               
               

print(is_prime(29)) # Should be True
print(is_prime(73)) # Should be True
print(is_prime(75)) # Should be False