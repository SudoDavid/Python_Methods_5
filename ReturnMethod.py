import sys
#hello
# Write performOperation function here
def performOperation(numberOne, numberTwo, Operation):
    if Operation == '+':
        result  = numberOne + numberTwo
        return result
    elif Operation == '-':
        result  = numberOne - numberTwo
        return result
    elif Operation == '/':
        result  = numberOne / numberTwo
        return result
    elif Operation == '*':
        result  = numberOne*numberTwo
        return result
    else:
        sys.exit


numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
operation = input("Enter an operator (+ - * /): ")

# Call performOperation method here and store the value in "result"
performOperation(numberOne,numberTwo,operation)

print(str(numberOne) + " " + operation + " " + str(numberTwo) + " = " + str(result))
