def f(x):
    return 2*x**3 + 4*x + 5

def df(x):
    return 6*x**2 + 4

def gradient_descent(learning_rate, epochs, initial_x):
    x = initial_x
    for _ in range(epochs):
        grad = df(x)
        x = x - learning_rate * grad
    return x

if __name__ == '__main__':
    try:
        lr = float(input("Enter learning rate (e.g. 0.01): "))
        epochs = int(input("Enter number of iterations (e.g. 1000): "))
        initial_x = float(input("Enter initial value of x (e.g. 0): "))
    except ValueError:
        print("Invalid input.")
        exit()

    min_x = gradient_descent(lr, epochs, initial_x)
    print(f"Value of x at which function is minimum (approx.): {min_x}")
    print(f"Minimum value of function (approx.): {f(min_x)}")
