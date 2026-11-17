balance = 10000
pin = 1234
count = 0
login = False

# Check PIN
while count < 3:
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("Login Successful")
        login = True
        break
    else:
        print("Wrong PIN")
        count += 1

if login:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("5. Change PIN")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your Balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))

            if amount < 0:
                print("Invalid Amount")
                continue
            else:
                balance += amount
                print("Amount Deposited")
                print("New Balance:", balance)

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))

            if amount < 0:
                print("Invalid Amount")
                continue
            elif amount > balance:
                print("Insufficient Balance")
            else:
                balance -= amount
                print("Please Collect Your Cash")
                print("Remaining Balance:", balance)

        elif choice == "4":
            print("Final Balance:", balance)
            print("Thank You")
            break

        elif choice == "5":
            print("Change PIN is not available")
            pass

        else:
            print("Invalid Choice")

else:
    print("Your ATM is Locked")
