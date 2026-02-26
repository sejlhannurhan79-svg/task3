n=input()
s=True
for i in range (len(n)):
    if int(n[i])%2==0:
        s=True
    else:
        s=False
        break
if s:
    print("Valid")
else:
    print("Not valid")
    
