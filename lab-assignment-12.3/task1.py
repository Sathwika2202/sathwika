def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == '__main__':
    lst = input("Enter list elements separated by spaces: ").split()
    # Try converting to ints if possible
    try:
        lst = [int(x) for x in lst]
    except ValueError:
        pass  # keep as strings if not all are numbers
    target = input("Enter value to search: ")
    # Try converting target type to match list
    if lst and isinstance(lst[0], int):
        try:
            target = int(target)
        except ValueError:
            pass
    idx = linear_search(lst, target)
    if idx != -1:
        print(f"Value found at index: {idx}")
    else:
        print("Value not found in list.")
