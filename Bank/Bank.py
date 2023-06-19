import User

print("Welcome to the Bank of Blooket!")


print("Thank you for using the Bank of Blooket!, Your options are:\n",
        "1. Open an account\n",
        "2. Withdraw Money from bank\n",
        "3. Deposit Money\n",
        "4. View balance\n",
        "5. Close Account\n"
     )

Bob = User("Bob", "Nugget", "BNugget", "chicken52", 1234658, 5)

choice = int(input("Which one would you like to do?"))

if choice == "open an account":
    print("Thank you for opening an account")
if choice == "withdraw toast":
    print("How much toast would you like?")

# use either an if then OR a Match case for the homework

match choice:
    case 1:
        print("Thanks for opening an account with The Bank of Blooket")
    case 2:
        print("how much would you like to withdraw?")
    
