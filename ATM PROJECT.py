#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import sys
class ATM():
    def __init__(self,owner,balance,account_number):
        self.owner=owner
        self.balance=balance
        self.account_number=account_number
    
    def details(self):
        print(f"\n---------ACCOUNT DETAILS---------\nAccount owner: {self.owner}\nAccount balance: {self.balance} euros\nAccount number: {self.account_number}\n----------------------------------")
                   
    def deposit(self, deposit_amount):
        self.deposit_amount= deposit_amount
        self.balance = self.balance + self.deposit_amount
        print('Deposit Accepted')
        print(f"Added {deposit_amount} in your balance")
        print(f"The new amount of your bank account is: {self.balance} euros")
        
    def withdraw(self,withdraw_amount):
        self.withdraw_amount=withdraw_amount
        if self.withdraw_amount>self.balance:
            print('Insufficient Amount')  
        else:
            self.balance=self.balance-self.withdraw_amount
            print('Withdrawal accepted')
            print(f"Withdrawn {withdraw_amount} from your balance")
            print(f"The new amount of your bank account is: {self.balance} euros")
            
    def check_balance(self):
        print(f"Your account balance is: {self.balance}")
        
    def change_PIN(self,PIN):
        self.PIN=PIN
        while True:
            new_PIN=int(input("Your PIN number should only be 4 digits. Please enter 4 digits only: "))
            if len(str(new_PIN))==4:
                print(f"Your PIN number has been succesfully changed to: {new_PIN}")
                break
            else:
                print (new_PIN)
                 
    def options(self):
        print("TRANSACTION\n******************\nMenu:\n1. Account Details\n2. Check Account Balance\n3. Deposit\n4. Withdraw\n5. Change PIN\n6. EXIT\n******************")
        while True:
            try:
                option=int(input("Please choose one of the above options by entering 1,2,3,4,5 or 6: "))
            except:
                print("error")
               
            else:
                if option==1:
                    atm.details()
                elif option==2:
                    atm.check_balance()
                elif option == 3:
                    deposit_amount = int(input("Please enter the amount you wish to deposit:"))
                    atm.deposit(deposit_amount)
                elif option==4:
                    withdraw_amount=int(input("Please enter the amount you wish to withdraw:"))
                    atm.withdraw(withdraw_amount)
                elif option==5:
                    atm.change_PIN(PIN)
                elif option==6:
                    print(f"printing receipt.........\n******************************************\nTransaction is now complete.\nTransaction number: {random.randint(10000, 1000000)}\nAccount owner: {self.owner}\nAccount number: {self.account_number}\nAvailable Balance: {self.balance}\nThank you for choosing THE BANK OF PYTHON\n******************************************")
                    break
                    sys.exit()
   
print("******WELCOME TO THE BANK OF PYTHON******")
print("________________________________________________")
owner=input("Please enter your full name: ")
balance=int(input("Please enter your balance: "))
account_number=input("Please enter your account number: ")
atm=ATM(owner,balance,account_number)
PIN=int(input("Please enter your 4-digit PIN number:"))
if len(str(PIN))==4:
    print("PIN NUMBER ACCEPTED")
    while True:
        trans=input("Do you wish to make any transaction?(Y/N): ")
        if trans=="Y" or trans=="y":
            atm.options()
        elif trans=="N" or trans=="n":
            print("Thank you for choosing the BANK OF PYTHON")
            break
        else:
            print("Wrong command. Please enter Y or N only. Thank you")            
else:
    print("INVALID PIN NUMBER LENGTH")


# In[ ]:




