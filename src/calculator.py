# Demo Calculator App For Week 1 Project
# Addition Method
def add(a, b):
    return a + b


# Subtract Method
def sub(a, b):
    return a - b



# Multiplication
def mul(a, b):
    return a * b


# Division
def div(a, b):
    return a / b


if __name__ == "__main__":
    # Input values
    a = 4
    b = 2

    # Perform calculations
    sum_result = add(a, b)
    diff_result = sub(a, b)
    product_result = mul(a, b)
    div_result = div(a, b)

    # Print results
    print(f"Sum of {a} and {b} is {sum_result}")
    print(f"Difference of {a} and {b} is {diff_result}")
    print(f"Product of {a} and {b} is {product_result}")
    print(f"Division of {a} and {b} is {div_result}")
