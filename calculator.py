 # if = does codes only if some conditons are true else does sth else

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result,4))
elif operator == "-":
    result = num1 - num2
    print(round(result,4))
elif operator == "*":
    result = num1 * num2
    print(round(result,4))
elif operator == "/":
    result = num1 / num2
    print(round(result,4))
else:
    print(f"{operator} operator selected is not valid")



