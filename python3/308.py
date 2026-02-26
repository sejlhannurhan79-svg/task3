def draw(b, a):
    if a > b:
        return "Insufficient Funds"
    else:
        return b - a


b, w = map(int, input().split())

result = draw(b, w)

print(result)