def calculate_bmi():
    weight = float(input("Enter your weight (in kilograms): "))
    height = float(input("Enter your height (in meters): "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        category = "Normal"
    elif bmi >= 25 and bmi < 30:
        category = "Overweight"
    else:
        category = "Unrecognized"

    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    calculate_bmi()