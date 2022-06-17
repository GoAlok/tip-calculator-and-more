
# Built the "BODY MASS INDEX Calculator"

# ** = power
# BMI = (WEIGHT(kg)) / (height ** 2 (m**2))
# ---------LET'S CODE---------

print('---- BMI CALCULATOR ----')

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# print("Height: ",type(height),", Weight: ", type(weight))
bmi = float(weight)/float(height)**2 
bmi_as_int = int(bmi)
print(bmi_as_int)
