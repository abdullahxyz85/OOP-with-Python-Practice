from Account import *

accountsDict = {}
nextAccountNumber = 0

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
    print()

    action = input("What do you want to do?")
    action = action.lower()
    action = action[0] # grab the first letter 
    print()

    if action == "b":
        print("*** Get Balance ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = input(userAccountNumber)
        userAccountPassword = input("Please enter the password: ")
        oAccount  = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print("Your balance is: ", theBalance)
    elif action == "d":
        print("*** Deposit *** ")
        userAccountNumber = input("Please enter the account number: ")
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input("Please enter amount to deposit:")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print("Your new balance is: ", theBalance)
    elif action == "o":
        print("*** Open Account ***")
        userName = input("What is the name for the new user account?")
        userStartingAmount = input("What is the starting balance for this account?")
        userStartingAmount = int(userStartingAmount)
        userPassword = input("What is the password you want to use for this account?")
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print("Your new account number is:", nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()
    elif action == "s":
        print("Show: ")
        for userAccountNumber in accountsDict:
            oAccount  = accountsDict[userAccountNumber]
            print("     Account Number: ", userAccountNumber)
            oAccount.show()
    elif action == "q":
        break
    elif action == "W":
        print("*** Withdraw ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input("Please enter the amount to withdraw: ")
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input("Please enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)
        if theBalance is not None:
            print("Withdraw:", userWithdrawalAmount)
            print("Your new balance is:", theBalance)
    else:
        print("Sorry, that was not a valid action. Please try again.")
    print("Done")