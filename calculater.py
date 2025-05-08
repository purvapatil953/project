
print("***MY CALCULATER***\n\n")
n1 = float(input("Enter number: "))
n2 = float(input("Enter number: "))
print("\n\nEnter operation (+, -, *, /):")
operator = input("Enter operator: ")

match operator:
    case '+':
        result = n1 + n2
    case '-':
        result = n1 - n2
    case '*':
        result = n1 * n2
    case '/':
        if n2!=0:
            result = n1 / n2
        else:
            result = "not division by zero"
    case _:
        result = "Invalid"

print(f"\nResult: {n1} {operator} {n2} = {result}")


