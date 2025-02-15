def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
keep = False
while True:
    if not keep:
        n1 = float(input("What is the first number?: "))
    for ops in operations:
        print(ops)
    op = input("Pick an operation: ")
    n2 = float(input("What is the next number?: "))
    result = operations[op](n1,n2)
    print(f"{n1} {op} {n2} = {result}")
    if input(f"Type 'y' to keep calculating with {result}, or type 'n' to start a new calculation: ").lower() == 'y':
        keep = True
        n1 = result
    else:
        keep = False


