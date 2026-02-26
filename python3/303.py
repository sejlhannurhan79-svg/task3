s = input()
to_digit = {
    "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7",
    "EIG": "8", "NIN": "9", "ZER": "0"
}
word = {v: k for k, v in to_digit.items()}
for op in "+-*":
    if op in s:
        first, second = s.split(op)
        operator = op
        break
def convert(st):
    num = ""
    for i in range(0, len(st), 3):
        num += to_digit[st[i:i+3]]
    return int(num)
a = convert(first)
b = convert(second)
if operator == "+":
    res= a + b
elif operator == "-":
    res = a - b
else:
    res = a * b
r = str(res)
answer = ""
for j in r:
    answer += word[j]
print(answer)