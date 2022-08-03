lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']

result = list(filter(lambda line: True if line.count('11') else False, lines))
print(len(lines) - len(result))
