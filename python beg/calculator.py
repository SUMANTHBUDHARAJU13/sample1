def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
operation={
    "+":addition,
    "-":subtraction,
    "*":multiply,
    "/":division
}
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
for i in operation:
    print(i)
operation_symbol=input("Enter any operation you want to perform: ")
calculation=operation[operation_symbol]
answer=calculation(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")