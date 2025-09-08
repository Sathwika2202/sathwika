def greet_user(name, gender):
    gender = gender.lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Mrs."
    else:
        title = "Mx."
    return f"Hello, {title} {name}! Welcome."

# Example function calls
print(greet_user("Alex", "male"))
print(greet_user("Taylor", "female"))
print(greet_user("Sam", "non-binary"))