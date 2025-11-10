# Simple Python Calculator

This is a basic command-line calculator written in Python.  
It allows the user to perform simple arithmetic operations — addition, subtraction, multiplication, and division.

## 🧮 Features
- Accepts two numerical inputs from the user  
- Supports four basic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Displays the result in a clear format  
- Handles invalid operation choices gracefully  

## 📜 Code Example

```python
a = int(input("Enter 1st Number :- "))
b = int(input("Enter 2nd Number :- "))
choice = input("Enter your choice +,-,*,/ :- ")

if choice == '+':
    print(a, "+", b, ":-", a + b)
elif choice == '-':
    print(a, "-", b, ":-", a - b)
elif choice == '*':
    print(a, "*", b, ":-", a * b)
elif choice == '/':
    print(a, "/", b, ":-", a / b)
else:
    print("Invalid choice")
