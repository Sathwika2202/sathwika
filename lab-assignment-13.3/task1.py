def rectangle_area(x, y):
    return x * y

def square_area(x):
    return x * x

def circle_area(x):
    return 3.14 * x * x

def calculate_area(shape, x, y=0):
    area_functions = {
        "rectangle": lambda x, y: rectangle_area(x, y),
        "square": lambda x, _: square_area(x),
        "circle": lambda x, _: circle_area(x)
    }
    func = area_functions.get(shape.lower())
    if not func:
        raise ValueError("Unsupported shape")
    return func(x, y)

if __name__ == "__main__":
    shape = input("Enter shape (rectangle, square, circle): ").strip().lower()
    if shape == "rectangle":
        x = float(input("Enter length: "))
        y = float(input("Enter width: "))
        area = calculate_area(shape, x, y)
    elif shape == "square" or shape == "circle":
        x = float(input("Enter side (for square) or radius (for circle): "))
        area = calculate_area(shape, x)
    else:
        print("Unsupported shape")
        exit(1)
    print(f"Area of {shape}: {area}")
