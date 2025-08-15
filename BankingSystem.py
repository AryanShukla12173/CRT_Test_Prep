from abc import ABC, abstractmethod
import datetime
class Person:
    def __init__(self,name,address,phone):
        if len(name) == 0 or  len(address) == 0 or len(phone) == 0:
            print("Values cannot be empty")
            return 0
        else:
            self.name = name
            self.address = address
            self.phone = phone
    def get_details(self):
        return [self.name,self.phone,self.address]
    
# 13.	Account (Abstract)
# 14.	Attributes:
# -	account_number (str): Unique identifier for the account
# -	balance (float): Current balance of the account
# -	owner (Customer object): Owner of the account
# 15.	Methods:
# -	deposit(amount): Adds funds to the account
# -	withdraw(amount): Deducts funds, ensuring no overdrafts occur in general
# -	get_balance(): Returns the current balance
# -	show_account_details(): Displays account details

class Account(ABC):
    account_id_count = 0
    def __init__(self,owner):
        self.account_number = Account.account_id_count + 1
        self.balance = 0.00
        self.owner = owner
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def get_balance(self):
        pass
    @abstractmethod
    def show_account_details(self):
        pass

# 16.	Customer (Inherits from Person)
# 17.	Attributes:
# -	accounts (list of Account objects): All accounts linked to the customer
# 18.	Methods:
# -	add_account(account): Adds a new account to the customer's account list
# -	remove_account(account_number): Removes an account from the customer’s list
class Customer(Person):
    def __init__(self, name, address, phone):
        super().__init__(name, address, phone)
        self.accounts = []
        Bank.customers.append([name,address,phone])
    def add_account(self,account):
        self.accounts.append(account)
    def remove_account(self,account_number):
        for idx,i in enumerate(self.accounts):
            if i == account_number:
                self.accounts = self.accounts[idx:]
                break
                

# 19.	Admin (Inherits from Person)
# 20.	Attributes:
# -	employee_id (str): Unique identifier for the admin
# 21.	Methods:
# -	approve_account(customer, account): Approves and activates a new account
# -	view_all_customers(): Provides a summary of all bank customers

class Admin(Person):
    def __init__(self, name, address, phone,employee_id):
        super().__init__(name, address, phone)
        self.employee_id = employee_id
        Bank.admins.append({employee_id,name,address,phone,address})
    def approve_account(self,customer,account):
        accountType = account.accountType
        
        if accountType == 1:
            new_account = SavingsAccount(account)
        else:
            new_account = BusinessAccount(account)
        new_customer = Customer(**account)
        new_customer.add_account(new_account)
         
    def view_all_customers(self):
        pass


# 22.	SavingsAccount (Inherits from Account)
# 23.	Attributes:
# -	interest_rate (float): Interest rate for the savings account
# 24.	Methods:
# -	apply_interest(): Calculates and applies interest to the account balance periodically

class SavingsAccount(Account):
    transaction_id = 0
    interest_rate = 0.05
    def __init__(self, owner):
        super().__init__( owner)
        
    def apply_interest(self):
        pass
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            new_transaction = Transaction(SavingsAccount.transaction_id+1,"Deposit",amount,{"date":datetime.date, "time":datetime.time})
            
        else:
            print("Given amount is negative")
        
    def withdraw(self,amount):
        if self.balance < 0:
            print("Insufficient Funds for Withdrawing")
        else:
            self.balance -= amount
            new_transaction = Transaction(SavingsAccount.transaction_id+1,"Withdraw",amount,{"date":datetime.date, "time":datetime.time})
            
    def get_balance(self):
        if self.balance > 0:
            print(f"Current Available Balance:{self.balance}")
        else:
            print("Insufficient Balance")
    def show_account_details(self):
       print(self.owner)

    
        

# 25.	BusinessAccount (Inherits from Account)
# 26.	Attributes:
# -	overdraft_limit (float): Limit for overdrafts
# 27.	Methods:
# -	Override withdraw(amount): Allows withdrawal within the overdraft limit
class BusinessAccount(Account):
    id_counter = 100
    overdraft_limit = 0.0
    def __init__(self,owner):
        super().__init__(owner)
        self.withdrawal_count = 0.0
        
    def withdraw(self,amount):
        if self.withdrawal_count > BusinessAccount.overdraft_limit:
            print("Overdraft Limit Exceeded")
        else:
            self.balance -= amount
            self.withdrawal_count += 1
            new_transaction = Transaction(BusinessAccount.id_counter+1,"Withdraw",amount,{"date":datetime.date, "time":datetime.time})
           
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            new_transaction = Transaction(BusinessAccount.id_counter+1,"Deposit",amount,{"date":datetime.date, "time":datetime.time})
          
    def get_balance(self):
        if self.balance > 0:
            print(f"Current Available Balance:{self.balance}")
        else:
            print("Insufficient Balance")
    def show_account_details(self):
       print(self.owner)

# 28.	Transaction
# 29.	Attributes:
# -	transaction_id (str): Unique identifier for the transaction
# -	transaction_type (str): Type of transaction ("Deposit" or "Withdrawal")
# -	amount (float): Amount transacted
# -	date (datetime): Date of the transaction
# 30.	Methods:
# -	get_transaction_details(): Returns the transaction details

class Transaction:
    transactions = []
    def __init__(self,transaction_id,transaction_type,amount,datetime):
        self.transaction_id = transaction_id
        self.transaction_type =transaction_type
        self.amount = amount
        self.datetime = datetime
        Transaction.transactions.append({transaction_id,transaction_type,amount,datetime})
    def get_transaction_details(self):
        print(f'Transaction ID : {self.transaction_id},Transaction Type: {self.transaction_type},Transaction Amount:{self.amount}, Transaction Date and Time :{self.datetime}')
    
# 31.	Bank
# 32.	Attributes:
# -	customers (list of Customer objects): All bank customers
# -	admins (list of Admin objects): All bank admins
# 33.	Methods:
# -	create_customer_account(): Initiates a new account creation for a customer
# -	delete_customer_account(): Deletes a customer’s account
# -	view_transaction_history(account_number): Returns all transactions for a given account
# -	find_customer_by_account(account_number): Finds and returns the customer associated with an account

class Bank :
    customers = []
    admins = []
    def create_customer_account():
        while True:
                name = input("Enter Your Name:")
                address = input("Enter Your Phone:")
                phone = input("Enter Your 10 digit Phone Number:")
                accountType = int(input("Enter Type of Account : 1)Savings Account 2)Buisness Account"))
                if len(name) == 0 or  len(address) == 0 or len(phone) == 0 or len(phone) < 10 or accountType not in [1,2]:
                    print("Values cannot be empty")
                    print("No. of Digits in Phone Number is incorrect")
                    print("Enter the assigned Digit for the Account Type")
                else:
                    break
        admin = Admin('xyz','zyz','1000000000', 1)
        admin.approve_account({name,address,phone})
    
    def view_transaction_history(self,account_number):
        pass
    def find_customer_by_account(account_number):
        pass
        
            
            
            
            
                    
                
                
                
