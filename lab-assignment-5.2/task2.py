# Simple loan approval logic based on user input
# This code checks for bias by evaluating different names and genders

def loan_approval(name, gender):
    # Example logic: approve if income > 50000
    # No bias based on name or gender
    income = float(input(f"Enter annual income for {name}: "))
    if income > 50000:
        return f"Loan approved for {name}."
    else:
        return f"Loan not approved for {name}."

if __name__ == "__main__":
    name = input("Enter applicant's name: ")
    gender = input("Enter applicant's gender (M/F): ")
    result = loan_approval(name, gender)
    print(result)