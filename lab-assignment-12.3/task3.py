def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    lst = input("Enter sorted list elements separated by spaces: ").split()
    # Try converting inputs to ints
    try:
        lst = [int(x) for x in lst]
    except ValueError:
        pass  # Keep as strings if not all are ints

    target = input("Enter value to search: ")
    if lst and isinstance(lst[0], int):
        try:
            target = int(target)
        except ValueError:
            pass

    idx = binary_search(lst, target)
    if idx != -1:
        print(f"Value found at index: {idx}")
    else:
        print("Value not found in list.")
