nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda num: num**2, nums))
new_nums = list(filter(lambda num: num % 2 == 0, squares))
print(new_nums)
