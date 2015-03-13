a = input("Enter A: ")
a = int(a)
b = input("Enter B: ")
b = int(b)
oper = input("Enter operation: ")

if oper == "+":
    result = a + b
    print("Result is {}".format(result))
elif oper == "-":
    result = a - b
    print("Result is {}".format(result))
elif oper == "*":
    result = a * b
    print("Result is {}".format(result))
elif oper == "/":
    result = a / b
    print("Result is {}".format(result))
else:
    print("We dont support {}".format(oper))