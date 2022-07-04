wzrost = float(input("Podaj swój wzrost (w m): "))
waga = float(input("Podaj swoją wagę (w kg): "))

bmi = waga / (wzrost**2)
print("Twoje BMI to: ",round(bmi,2))