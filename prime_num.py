import math

def is_prime(num):
    
    if not isinstance(num, int) or (num)<2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

    