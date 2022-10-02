print("Operations are: *, /, +, -, F, @")

def get_inputs():
    no1 = float(input("Please input your first number: "))
    no2 = float(input("Please input your second number: "))
    o = input('operation: ')
    return no1, no2, o

def calculate(no1, no2, o):
    if o == '+':
        result = no1 + no2
    elif o == '@':
        result = (no1 + no2/12) * 7
    elif o == '*':
        result = (no1 * no2)
    elif o == 'F':
        result = no1 * 9/5 + 32
    elif o == '/':
        result = (no1/no2)
    elif o == '-':
        result = no1 - no2
    return result
