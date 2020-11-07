def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return('not prime')    
    return 'prime'
print(is_prime(17))
print(is_prime(3456))
print(is_prime(345))
print(is_prime(71))