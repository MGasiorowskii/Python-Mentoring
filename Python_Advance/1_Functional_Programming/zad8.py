orders = [
["34587", "Learning Python, Mark Lutz", 4, 40.95],
["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3, 32.95],
["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
]

prices = list(map(lambda order: round(order[2] * order[3], 2), orders))
new_prices = list(map(lambda x: x + 10 if x < 100 else x, prices))
idx = list(map(lambda order: order[0], orders))

invoice = list(map(lambda idx, price: (idx, price), idx, new_prices))

print(invoice)

