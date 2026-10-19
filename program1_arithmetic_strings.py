"""Question: Accept two numbers and a string from the user.
Perform arithmetic operations (+, -, *, /, //, %, **) on the numbers and string operations
 (concatenation, repetition, slicing, case conversion)."""

# Program 1: Arithmetic and String Operations

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
s = input("Enter a string: ")

print("\nArithmetic Operations")

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
    print("Floor Division =", a // b)
    print("Modulus =", a % b)
else:
    print("Division is not possible")
    print("Floor Division is not possible")
    print("Modulus is not possible")

print("Power =", a**b)

print("\nString Operations")

print("Concatenation =", s + " Python")
print("Repetition =", s * 2)
print("Slicing =", s[0:3])
print("Uppercase =", s.upper())
print("Lowercase =", s.lower())
