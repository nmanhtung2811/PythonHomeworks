'''score = 100
if score >= 90:
    print("grade is A")
elif score >= 80 and score < 90:
    print("grade is B")
elif score >= 70 and score < 80:
    print("grade is C")
elif score >= 60 and score < 70:
    print("grade is D")
else:
    print("grade is F")'''


weight = 300
height = 100
BMI = weight*703/height**2
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25.0:
    print("Normal")
elif BMI >= 25.0 and BMI < 30.0:
    print("Overweight")
else:
    print("Obese")

