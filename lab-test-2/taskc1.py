def rotate_matrix(matrix):
    """
    Rotates an NxN matrix 90 degrees clockwise in-place.
    Args:
        matrix (List[List[int]]): NxN matrix to rotate
    Returns:
        None (modifies matrix in-place)
    """
    n = len(matrix)
    if n == 0 or n != len(matrix[0]):
        raise ValueError("Input must be a non-empty NxN matrix")
    # Layer by layer rotation
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # save top
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top

# --- TESTS ---

def print_matrix(m):
    for row in m:
        print(row)
    print()

def test_rotate_matrix():
    # 1x1
    m1 = [[1]]
    rotate_matrix(m1)
    assert m1 == [[1]], f"Failed 1x1: {m1}"

    # 2x2
    m2 = [
        [1, 2],
        [3, 4]
    ]
    rotate_matrix(m2)
    assert m2 == [
        [3, 1],
        [4, 2]
    ], f"Failed 2x2: {m2}"

    # 3x3
    m3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_matrix(m3)
    assert m3 == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ], f"Failed 3x3: {m3}"

    # 4x4
    m4 = [
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    rotate_matrix(m4)
    assert m4 == [
        [13,  9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ], f"Failed 4x4: {m4}"

    print("All tests passed.")

if __name__ == "__main__":
    # Example: read matrix from console, rotate, print
    import ast
    s = input("Enter NxN matrix (e.g. [[1,2],[3,4]]): ")
    matrix = ast.literal_eval(s)
    rotate_matrix(matrix)
    print("Rotated matrix:")
    print_matrix(matrix)
    # Run tests
    test_rotate_matrix()
