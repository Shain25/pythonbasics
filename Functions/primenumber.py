def is_prime (num: int):
    if num>1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False
    
print(is_prime(7))
print(is_prime(5))
print(is_prime(10))
print(is_prime(1))