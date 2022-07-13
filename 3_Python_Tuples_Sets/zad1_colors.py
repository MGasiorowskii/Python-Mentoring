colors = [ 'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny',
           'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']

unique_colors = set(colors)
print(unique_colors)

print(f"Number of all elements: {len(colors)}")
print(f"Number of unique colors: {len(unique_colors)}")

for color in unique_colors:
    print(color)

unique_colors.add("biały")
print(unique_colors)

unique_colors.remove("zielony")
print(unique_colors)
