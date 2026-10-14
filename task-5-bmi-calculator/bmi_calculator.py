
def calculate_bmi(weight, height):
    return weight / (height * height)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== BMI Calculator ===")
    print("Enter your weight in kilograms and height in meters.")

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print("BMI Category:", category)

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
