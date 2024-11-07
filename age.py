def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden age"
    else:
        return f"Invalid age: {age}"

def main():
    try:
# Get age input from the user
        age = int(input("Enter the age: "))
# Categorize and display the result
        category = categorize_by_age(age)
        print(f"Life stage: {category}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

if __name__ == "__main__":
    main()