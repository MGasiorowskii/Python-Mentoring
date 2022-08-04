three_d = [[[1, 2, 3, 4],
[0, -1, -2, -3, -4, -5, -6]],
[[1, 10, 15, 12, 20, 20, 20],
[-15, -13, 14, 20, -1]]
]

filtered = [x for sublist in three_d
            for x in sublist
            if len(x) > 4]

print(filtered)
