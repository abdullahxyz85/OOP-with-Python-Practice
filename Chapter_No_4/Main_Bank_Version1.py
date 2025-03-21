from Account import *
oJoesAccount = Account("Joe", 100, "JoesPassword")
print("Created an account for Joe")

oMarysAccount = Account("Mary", 12345, "MarysPassword")
print("Ceated an account for Mary")

oJoesAccount.show()
oMarysAccount.show()
print()

print("Calling methods of the two accounts")
oJoesAccount.deposit(50, "JoesPassword")
oMarysAccount.withdraw(345, "MarysPassword")
oMarysAccount.deposit(100, "MarysPassword")

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()


# create another account with information from the user
print()
userName = input("What is the name for the new user account?")
userBalance = input("What is the starting balance for this account?")
userBalance = int(userBalance)
userPassword = input("What is the password you want to use for this account")

oNewAcount = Account(userName, userBalance, userPassword)

# Show the newly created user account
oNewAcount.show()

#lets deposit 100 into the new account
oNewAcount.deposit(100, userPassword)
userBalance = oNewAcount.getBalcance(userPassword)
print()
print("After depositing 100, the user's balance is:", userBalance)

# Show the new account
oNewAcount.show()