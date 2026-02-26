nums = list(map(int, input().split()))

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True


primes = []

for num in nums:
    if is_prime(num):
        primes.append(num)


if len(primes) > 0:
    print(*primes)
else:
    print("No primes")