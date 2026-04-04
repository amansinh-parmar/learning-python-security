def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y != 0:
        return x / y
    else:
        print("Error! Divided by zero.")

def calculator():
    print("<<CALCULATOR>>\n")
    print("Select Option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter your choice: ")

        if choice in ['1','2','3','4']:
            try:
                num1 = float(input("Enter First Number:"))
                num2 = float(input("Enter Second Number:"))
            except ValueError:
                print("Invalid Input! Please select 1,2,3 or 4.")

            if choice == '1':
                print(f"Add:{int(num1)}+{int(num2)}={add(num1,num2)}")
            elif choice == '2':
                print(f"Subtract:{int(num1)}-{int(num2)}={subtract(num1,num2)}")
            elif choice == '3':
                print(f"Multiply:{int(num1)}x{int(num2)}={multiply(num1,num2)}")
            elif choice == '4':
                print(f"Divide:{int(num1)}/{int(num2)}={divide(num1,num2)}")
        else:
            print("Invalid choice! Please enter valid input.")


        next_calculation = input("Do you want to calculate again? (yes/no):")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()   