data = input().split()

role = data[0]
name = data[1]
salary = int(data[2])

if role == "Manager":
    bonus = int(data[3])
    total = salary + salary * bonus / 100

elif role == "Developer":
    projects = int(data[3])
    total = salary + projects * 500

else:  
    total = salary

print(f"Name: {name}, Total: {total:.2f}")