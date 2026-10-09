# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     return num1 / num2
    

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient balance!")
        return balance
    elif amount <= 0:
        print("Please enter a valid amount!")
        return balance
    else:
        return balance - amount

def check_balance(balance):
    return balance