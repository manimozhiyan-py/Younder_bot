import math

def prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2,int(math.sqrt(number))):
        if number%i == 0:
            return False
    return True

number = 11
print(prime(number))