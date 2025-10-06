numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
squares = [n ** 2 for n in numbers]
print(squares)
