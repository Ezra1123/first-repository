import random
import pymysql_lib

class Bank():

    logged_user = ""
    balance = 0

    def get_new_acct_no(self):

        new_acct = random.choice(range(1,9999999999))
        max_chars = 8
        current_acct_chars = len(str(new_acct))

        deficiency = max_chars - current_acct_chars

        if  deficiency:
            new_acct = ("0"*deficiency) + str(new_acct)
        
        return new_acct

    def register(self):
        
        name = input("Please enter your name - ")
        age = int(input("Please enter your age - " ))
        password = input("Please enter your password - ")

        pymysql_lib.add_user(name, age, password,self.get_new_acct_no())
        print("Successfully created account \n")

    def login(self):

        name_input = input("Please enter your name - ")
        password_input = input("Please enter your password - ")

        data = pymysql_lib.fetche_user_details(name_input)
        if data:
            print("Username was correct ..!!")
            if password_input == data[0]['password']:
                print("Loggin Successfull..!!")
                    
                self.logged_user = name_input
                self.balance = data[0]['balance']
                
            else:
                print("Sorry your password was wrong")

        else :
            print("Username was wrong ..!!")

    def read_data(self):
        
        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            acct_no = splitted_line[2]
            balance = splitted_line[3]

            print("###########################")
            print("Name :", name)
            print("Acct :", acct_no)
            print("- - - - - - - - - - - - - - ")
            print("\nBalance :\n", balance)
            print("###########################\n")


    def read_user_data(self):
        
        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(":;")
            name = splitted_line[0]
            title = splitted_line[1]
            body = splitted_line[2]

            if name == self.logged_user:
                print("###########################")
                print("Name :", name)
                print("Title :", title)
                print("- - - - - - - - - - - - - - ")
                print("\nBody :\n", body)
                print("###########################\n")

    def get_balance(self):

        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            acct_no = splitted_line[2]
            balance = splitted_line[3]

            if name == self.logged_user:

                data = {"name":name, "acct_no":acct_no, "balance":balance}
                print(data)
                return data

    def deposit(self, amount, name = "self"):

       

        target_name = name if name != "self" else self.logged_user
        original_balance = pymysql_lib.get_balance(target_name)[0]['balance']
        bal = int(original_balance) + amount
        pymysql_lib.alter_balance(target_name, bal)
        bal = int(bal) + amount

    
        print("Deposit Successfull...!")
    
    
    def withdraw(self, amount):

        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()
        file.close()

        temporary_container = ""

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            password = splitted_line[1]
            acct = splitted_line[2]
            bal = splitted_line[3]


            if self.logged_user == name:

                bal = int(bal) - amount

                line = f"{name},{password},{acct},{bal}"

            temporary_container += line + "\n"

        file = open(file_name, "w")
        file.write(temporary_container)
        print("Withdrawal Successfull...!")

    
    def transfer(self, amount, target):

        self.withdraw(amount)

        self.deposit(amount, target)
        

bank = Bank()
bank.deposit(28000, 'bolanle')