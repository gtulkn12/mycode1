#!/usr/bin/env python3
#!/usr/env python //////bad shebang line
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

operation = ""
def add(calc1,calc2):
    print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
  
def sub(num1,num2):
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))

def main():
    calc1 = 0.0
    calc2 = 0.0
    while calc1 != "q":
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input().lower().strip()
        if calc1 == "q":
            break
        try:
            calc1 = float(calc1)
        except: # ...if it breaks, do this instead
            print("Please enter a number ")
            continue # this will send you to the top of the while loop

        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input().lower().strip()
        if calc2 == "q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()
        if operation == "+":
            add(calc1,calc2)
        elif operation == '-':
            sub(calc1,calc2)
        else:
            print("\n Not a valid entry. Restarting...")

main()

def add(num1,num2):
    print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    
def sub(num1,num2):
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    

