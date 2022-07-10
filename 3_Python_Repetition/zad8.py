height = float(input("Input your height (w m): "))
weight = float(input("Input your weight (w kg): "))

bmi = weight / (height**2)
print("Your BMI is: ", round(bmi, 2))

if bmi < 18.5:
    print("You have underweight")
elif (bmi >= 18.5) and (bmi <= 24):
    print("You have healthy weight")
elif (bmi > 24) and (bmi <= 26.5):
    print("You have little overweight")
elif (bmi > 26.5) and (bmi < 30):
    print("You have overweight")
elif (bmi >= 30) and (bmi <= 35):
    print("You have overweight and obese level 1")
elif (bmi > 35) and (bmi <= 40):
    print("You have overweight and obese level 2")
else:
    print("You have overweight and obese level 3")

