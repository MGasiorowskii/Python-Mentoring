fuel_level = 0
numbers_of_astronauts = 0
height_of_rocket = 0

while (fuel_level <= 5000) or (fuel_level >= 30000):
    fuel_level = int(input("Input correct fuel level (5000-30000): "))

while 0 <= numbers_of_astronauts <= 7:
    numbers_of_astronauts = int(input("Input correct numbers of astronauts (0-7]: "))

while fuel_level >= 100:
    fuel_level -= 300 + (100 * numbers_of_astronauts)
    height_of_rocket += 100

if height_of_rocket >= 2000:
    print("Ship has reached orbit")
else:
    print("Ship hasn't reached orbit")
