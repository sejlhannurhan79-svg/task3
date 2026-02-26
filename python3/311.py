def add_pairs(a1, b1, a2, b2):
    return a1 + a2, b1 + b2

a1, b1, a2, b2 = map(int, input().split())

new_a, new_b = add_pairs(a1, b1, a2, b2)

print(f"Result: {new_a} {new_b}")