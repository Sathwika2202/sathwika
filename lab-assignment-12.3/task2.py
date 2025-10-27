def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in the right place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    lst = input("Enter list elements separated by spaces: ").split()
    # Try converting the elements to ints
    try:
        lst = [int(x) for x in lst]
    except ValueError:
        pass  # keep original types if conversion fails

    bubble_sort(lst)
    print("Sorted list:", lst)

    # Optionally, check if sorted
    is_sorted = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    print("Is the list sorted?", is_sorted)
