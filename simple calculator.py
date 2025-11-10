#Simple Calculator
# Take two numbers as input use conditionals statements use choice as variable for operations perform arithmetic.
a = int(input("Enter 1st Number :- "))
b = int(input("Enter 2nd Number :- "))
choice = input("Enter your choice +,-,*,/  :- ")
if choice == '+' :    print(a,"+",b,":- ",a+b)
elif choice == '-' :   print(a,"-",b,":- ",a-b)
elif choice == '*' :   print(a,"*",b,":- ",a*b)
elif choice == '/' :   print(a,"/",b,":- ",a/b)
else: print("Invalid choice")
