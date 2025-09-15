def merge_sorted_lists(list_a, list_b):
    """
    Merges two sorted lists into a single sorted list using the two-pointer technique.
    Preserves duplicates and stability (relative order of equal elements).
    Args:
        list_a (List[int]): First sorted list.
        list_b (List[int]): Second sorted list.
    Returns:
        List[int]: Merged sorted list.
    """
    merged = []
    i, j = 0, 0
    len_a, len_b = len(list_a), len(list_b)
    # Two-pointer technique: compare elements and append the smaller one
    while i < len_a and j < len_b:
        if list_a[i] <= list_b[j]:
            merged.append(list_a[i])
            i += 1
        else:
            merged.append(list_b[j])
            j += 1
    # Append any remaining elements from list_a
    while i < len_a:
        merged.append(list_a[i])
        i += 1
    # Append any remaining elements from list_b
    while j < len_b:
        merged.append(list_b[j])
        j += 1
    return merged

def test_merge_sorted_lists():
    # Normal case
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    # Unequal lengths
    assert merge_sorted_lists([1, 2, 3], [4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_sorted_lists([1, 4, 7, 9], [2, 3]) == [1, 2, 3, 4, 7, 9]
    # One empty list
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    # Both empty
    assert merge_sorted_lists([], []) == []
    # Duplicates
    assert merge_sorted_lists([1, 2, 2, 3], [2, 2, 4]) == [1, 2, 2, 2, 2, 3, 4]
    # All elements equal
    assert merge_sorted_lists([5, 5], [5, 5, 5]) == [5, 5, 5, 5, 5]
    # Negative numbers
    assert merge_sorted_lists([-3, -1, 2], [-2, 0, 3]) == [-3, -2, -1, 0, 2, 3]
    print("All tests passed.")

if __name__ == "__main__":
    import ast
    print("Enter first sorted list of order IDs (e.g. [1,3,5]):")
    a = input()
    print("Enter second sorted list of order IDs (e.g. [2,4,6]):")
    b = input()
    try:
        list_a = ast.literal_eval(a)
        list_b = ast.literal_eval(b)
        if not (isinstance(list_a, list) and isinstance(list_b, list)):
            raise ValueError
    except Exception:
        print("Invalid input. Please enter lists in Python list format, e.g. [1,2,3]")
    else:
        merged = merge_sorted_lists(list_a, list_b)
        print("Merged sorted list:")
        print(merged)
    # Run tests
    test_merge_sorted_lists()

# Explanation:
# The two-pointer technique works by maintaining an index for each list.
# At each step, compare the current elements of both lists.
# Append the smaller (or equal) element to the result and advance that pointer.
# When one list is exhausted, append the rest of the other list.
# This ensures O(n + m) time and preserves the order of duplicates.
