# Python follows the PEMDAS/BODMAS rule for arithmetic operations.
# Parentheses/Brackets, Exponents/Orders, Multiplication and Division (from left
# to right), Addition and Subtraction (from left to right). 
# Let's see some examples of arithmetic operations in Python.
# Addition
a = 10
b = 5
sum_result = a + b
print("Addition: ", sum_result)  # Output: 15
# Subtraction
sub_result = a - b
print("Subtraction: ", sub_result)  # Output: 5
# Multiplication
mul_result = a * b
print("Multiplication: ", mul_result)  # Output: 50
# Division
div_result = a / b
print("Division: ", div_result)  # Output: 2.0
# Floor Division
floor_div_result = a // b
print("Floor Division: ", floor_div_result)  # Output: 2
# Modulus
mod_result = a % b
print("Modulus: ", mod_result)  # Output: 0
# Exponentiation
exp_result = a ** b
print("Exponentiation: ", exp_result)  # Output: 100000
# Combined Operations
combined_result = (a + b) * (a - b) / b ** 2
print("Combined Operations: ", combined_result)  # Output: 3.0
# Note: In Python 3, the division operator (/) always performs floating-point division.
# For integer division, use the floor division operator (//).   
# You can also use parentheses to change the order of operations.
complex_result = (a + b) * (a - b) / (b ** 2)
print("Complex Operations with Parentheses: ", complex_result)  # Output: 3.0
# This is a simple demonstration of arithmetic operations in Python.    