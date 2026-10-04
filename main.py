from calc import add,sub,mul,div

def calculator(num1, num2, opr):

    if opr == "+" or opr == "add" or opr == "a":
        return add(num1, num2)
    elif opr == "-" or opr == "sub" or opr == "s":
        return sub(num1,num2)
    elif opr == "*" or opr == "mul" or opr == "m":
        return mul(num1,num2)
    elif opr == "/" or opr == "div" or opr == "d":
        return div(num1,num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opr = input("Enter operator: ")

if __name__ == '__main__':
    print(calculator(num1,num2,opr))