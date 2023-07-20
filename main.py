import calculator


selection = int(input("\nSelect your calculator operation: \
                  \n1. Addition\
                  \n2. Subtraction\
                  \n3. Multiplication\
                  \n4. Division \n"))

try:
    num1, num2 = map(int, input("\nProvide your 2 values: ").split())
except ValueError:
        print("Invalid input. Please enter only two integers.")


result = 0

if selection == 1:
    result = calculator.add(num1,num2)

elif selection == 2:
    result = calculator.subtract(num1,num2)

elif selection == 3:
    result = calculator.multiply(num1,num2)

elif selection == 4:
    divided = calculator.divide(num1,num2)
    result = round(divided, 3)

else:
    print("Something went wrong!!")

print(f"The end result of the operation is {result}.")