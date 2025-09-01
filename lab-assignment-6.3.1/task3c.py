def classify_age(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teen"
    elif age >= 20 and age <= 59:
        return "Adult"
    elif age >= 60:
        return "Senior"
    else:
        return "Invalid age"

# Take input from console
try:
    age = int(input("Enter your age: "))
    print(f"{age} years age group is {classify_age(age)}")
except ValueError:
    print("Please enter a valid integer for age.")