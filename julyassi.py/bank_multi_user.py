#THIS PART IS NOT THE CODE ITSELF THESE ARE JUST COMMANDS
def menu():
    money = int(5000)
    money = float(money)
    #print the options you have
    print "Welcome to the Python Bank System"
    print " "
    print "Your Transaction Options Are:"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "1) Deposit Money"
    print "2) Withdraw Money"
    print "3) Check Balance"
    print "4) Quit Python Bank System.pyw"
    print
    return input ("Choose your option: ")
#Here is the deposit part.... This is where the user inputs the amount of money
#they wish to deposit into their account.
def deposit(money):
    global balance
    deposit = input("How much: $")
    deposit = float(deposit)
    if deposit <= money:
        balance = balance + 1
        money = money - deposit
        money = float(money)
        deposit = deposit * .1
        deposit = float(deposit)
        balance = deposit + balance
        balance = float(balance)
        print "You've successfully deposited $", deposit, "into your account."
        print
        bank_balance(balance)
        return balance
#This is where the user inputs the amount of money they wish to withdraw from
#their account. Currently not programmed in as of yet.
def withdrawl(balance, money):
    print "Sorry, but this function is currently under construction!"
    print
    return
#This is an obvious one, this is where you check your balance.
def bank_balance(balance):
    print "Balance: $", balance
    return balance
# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
balance = 0
balance = float(balance)
money = 5000
money = float(money)
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        deposit = deposit(money)
    elif choice == 2:
        withdraw = withdrawl(balance, money)
    elif choice == 3:
        balance = bank_balance(balance)
    elif choice == 4:
        loop = 0
    print "Thank-You for stopping by the bank!"
#END OF THE PROGRAM