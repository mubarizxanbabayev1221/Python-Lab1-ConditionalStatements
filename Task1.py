weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height * height)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal Weight"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"
    
print(bmi)
print(category)