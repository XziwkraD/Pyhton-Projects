print("Welcome to Joel's arithmetic calculator!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quit")

while True:
    
    choice = float(input("Please select an option: "))
    
    if choice == 1:
        a = float(input("Enter your first value: "))
        b = float(input("Enter your second value here: "))
        print("The answer is: " + str(a+b))
        
    elif choice == 2:
        a = float(input("Enter your first value: "))
        b = float(input("Enter your second value here: "))
        print("The answer is: " + str(a-b))
        
    elif choice == 3:
        a = float(input("Enter your first value: "))
        b = float(input("Enter your second value here: "))
        ans = a*b
        print("The answer is:", ans)
        
    elif choice == 4:
        a = float(input("Enter your first value: "))
        b = float(input("Enter your second value here: "))
        ans = a/b
        print("The answer is:", ans)
        
    elif choice == 5:
        print("Thank You!")
        break