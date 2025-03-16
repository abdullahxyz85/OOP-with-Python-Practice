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