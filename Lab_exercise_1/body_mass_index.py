height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilogram: "))
# Body Mass Index is a simple calculation using a person's height and weigh
BMI = (weight / (height * height))
print("Your body mass index is:", BMI)