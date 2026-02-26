n = int(input())

def isUsual(num):
    if num <= 0:
        return False

    for p in (2, 3, 5):
        while num % p == 0:
            num //= p

    return num == 1

print("Yes" if isUsual(n) else "No")
