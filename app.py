# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

import addition
import subtraction
import multiplication
import division

choice = input("Enter choice(1/2/3/4: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", (num1 + num2))
    
elif choice == '2':
    print(num1, "-", num2, "=", (num1 - num2))
    
elif choice == '3':
    print(num1, "*", num2, "=", (num1 * num2))
    
elif choice == '4':
    print(num1, "/", num2, "=", (num1 / num2))

else:
    print("Invalid entry")
    
    
