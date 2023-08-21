print ("----Mini Calculator----")
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")
choice = int(input("Enter your choice from 1-4: "))
if choice == 1:
    print("The Addition of 2 numbers is:",num1 + num2)
elif choice == 2:
    print ("The Subtraction of 2 numbers is:",num1 - num2)
elif choice == 3:
    print ("The Multiplication of 2 numbers is:",num1 * num2)
elif choice == 4:
    print ("The Division of 2 numbers is:",num1 / num2)
else:
    print ("Invalid Input")
                    
