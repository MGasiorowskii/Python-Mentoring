def info_from_sets(number_set):
    print(f"Number of element in set: {len(number_set)}")
    print(f"Elements: {number_set}\n")


n = int(input("Input value of n: "))

A = set()
B = set()

for number in range(0, n+1, 2):
    A.add(number)

for number in range(2, n+1, 3):
    B.add(number)

print("C")
C = A | B
info_from_sets(C)

print("D")
D = A & B
info_from_sets(D)

print("E")
E = A - B
info_from_sets(E)

print("F")
F = B ^ A
info_from_sets(F)

print(f"If set B is contained in set A: {B.issubset(A)}")
