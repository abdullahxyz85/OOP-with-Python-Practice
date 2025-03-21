from Account import *
accountsList = []

# create two accounts
oAccount = Account("Joe", 100, "JoesPassword")
accountsList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account("Mary", 12345, "MarysPassword")
accountsList.append(oAccount)
print("Mary's account number is 1")

accountsList[0].show()
accountsList[1].show()
print()

# CAll some methods on the different accounts
print("Calling methods of the two accounts...")
accountsList[0].deposit(50, "JoesPassword")
accountsList[1].withdraw(345, "MarysPassword")
accountsList[1].deposit(100, "MarysPassword")

# Show the accounts:
accountsList[0].show()
accountsList[1].show()

#create another account with information from the user
print()
userName = input("What is the name for the new user account?")
userBalance = input("What is the starting balance for this account?")
userBalance = int(userBalance)
userPassword = input("What is the password you want to see for this  account?")
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)

print("Created new account, account number is 2")
accountsList[2].show()

accountsList[2].deposit(100, userPassword)
userBalance = accountsList[2].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is:", userBalance)

accountsList[2].show()