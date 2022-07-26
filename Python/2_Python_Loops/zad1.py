last_num = int(input("Input last number: "))

for num in range(last_num+1):
    print(f"{num}", end=' ')

print()
num = 0
while num <= last_num:
    print(f"{num}", end=' ')
    num += 1
