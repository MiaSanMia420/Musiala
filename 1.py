def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(a, b):
    primes = [num for num in range(a, b + 1) if is_prime(num)]
    return primes
a = int(input())
b = int(input())
result = find_primes_in_range(a, b)
print(" ".join(map(str, result)))
