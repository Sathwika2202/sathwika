# Test cases for assign_grade function from Task2.py

from Task2 import assign_grade

def run_tests():
    test_cases = [
        # Valid scores
        (95, "A"),
        (90, "A"),
        (89.9, "B"),
        (85, "B"),
        (80, "B"),
        (79.9, "C"),
        (75, "C"),
        (70, "C"),
        (69.9, "D"),
        (65, "D"),
        (60, "D"),
        (59.9, "F"),
        (0, "F"),
        (100, "A"),
        # Invalid scores
        (-1, "Invalid input"),
        (101, "Invalid input"),
        ("90", "Invalid input"),
        (None, "Invalid input"),
        ([90], "Invalid input"),
        ({'score': 90}, "Invalid input"),
    ]

    for i, (input_val, expected) in enumerate(test_cases):
        result = assign_grade(input_val)
        print(f"Test case {i+1}: assign_grade({repr(input_val)}) => {repr(result)} | Expected: {repr(expected)} | {'PASS' if result == expected else 'FAIL'}")

if __name__ == "__main__":
    run_tests()
