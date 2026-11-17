balance = 500
pin = 4321
attempts = 0

while attempts < 3:
    user_pin = int(input("Enter PIN: "))

    if user_pin == pin:
        print("Login Successful")
        break
    else:
        attempts += 1

if attempts == 3:
    print("Card Blocked")

else:
    while True:
        print("1. Check Balance")
        print("2. Recharge")
        print("3. Purchase")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Invalid Amount")
                continue
            balance += amount
            print("Recharge Successful")

        elif choice == "3":
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Invalid Amount")
                continue
            elif amount > balance:
                print("Insufficient Balance")
            else:
                balance -= amount
                print("Purchase Successful")

        elif choice == "4":
            pass

        elif choice == "5":
            print("Final Balance:", balance)
            break

        else:
            print("Invalid Choice")