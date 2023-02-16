print("\t\tWelcome to pima mwili program!")
weight = int(input("Enter your weight in Kg: "))
height = float(input("Enter your height in metres: "))

bmi = int(weight/height**2)
print(f"Your Body mass index is {bmi}.")

if bmi < 18.5:
    print("You are underweight mehn, work on yourself.")

elif bmi < 25:
    print("You have a normal weight. Keep up")

elif bmi < 30:
    print("You are overweight. Work out")

elif bmi < 35:
    print("You are obese mehn, try the gym")

else:
    print("You are clinically obese, see the doctor for further instructions")
