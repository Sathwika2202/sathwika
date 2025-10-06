items = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter number to search for: "))
print("Found" if target in items else "Not Found")
