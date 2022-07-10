d = (1, [2, 4], "text", 3+5j)

print(d[len(d)-1])
print(d[0])
print(d[1])

if "abc" in d:
    print("abc belong to tuple")
else:
    print("abc doesn't below to tuple")