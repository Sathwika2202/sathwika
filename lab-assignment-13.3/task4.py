# Refactored code using list comprehension and taking input from the console

nums = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in nums.strip().split()]
squares = [i * i for i in nums]
print("Squares:", squares)
