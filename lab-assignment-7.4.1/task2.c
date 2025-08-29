def sort_list(data):
    return sorted(data, key=lambda x: (isinstance(x, str), x))

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))