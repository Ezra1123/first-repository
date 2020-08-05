def deposit(money):
    global balance
    deposit = input("How much: #")
    deposit = float(deposit)
    if deposit <= money:
        balance = balance + 1
        money = money - deposit
        money = float(money)
        deposit = deposit * .1
        deposit = float(deposit)
        balance = deposit + balance
        balance = float(balance)
        print("You've successfully deposited #", deposit, "into your account.")
        print
        bank_balance(balance)
        return balance