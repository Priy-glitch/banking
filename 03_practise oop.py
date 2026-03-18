'''Question = Create student class that takes name & marks of 3 subjects as arguments 
  constructor ?
  then create a method to print the average.'''

#   Answer

# class Student:
#     def __init__(self,name,marks_of_3_subject ):
#         self.name_of_student = name
#         self.marks_of_all_subject = marks_of_3_subject 

#     def average(self):
#         print(f"The average of all marks is {sum(self.marks_of_all_subject)/3}")

# s1 =Student("Ayush",[50,50,45])
# print(s1.name_of_student,s1.marks_of_all_subject)
# s1.average()

""" Question 2}  _______

Create Account class with 2 attributes - balance & account no.
Create method for debit and credit & printing the balnace."""

# Answer mine

class Student:
    def __init__(self,balance,account_no):
        self.user_balance = balance
        self.user_account = account_no

    def Credit(self,amount):
        self.user_balance += amount
        print(f"credited amount is ; {amount}")                             # """   we can print our method argument  directly       """
        print(f"Total banace is ; {self.user_balance}")

    def Debit(self,amount):
        self.user_balance -= amount
        print(f"debited amount is ; {amount}")                              # """   we can print our method argument  directly       """
        print(f"Total balance is ; {self.user_balance}")

    def get_bal(self):
        print(self.user_balance)


acc1 = Student(10000,63744941050)
print(f"This user balance is {acc1.user_balance}, and the account number is {acc1.user_account}" )
acc1.Credit(700)
acc1.Debit(500)
acc1.get_bal()


# Ai answered

class Account:
    def __init__(self, balance, account_number):
        self.bal = balance
        self.account_id = account_number

    def credit(self, amount):
        self.bal += amount
        print(f"Amount credited: {amount}")
        print(f"Total balance is now: {self.bal}")

    def debit(self, amount):
        if amount > self.bal:
            print("Insufficient balance!")
        else:
            self.bal -= amount
            print(f"Amount debited: {amount}")
            print(f"Total balance after debit: {self.bal}")

    def total(self):
        print(f"Current balance: {self.bal}")


# Usage
acc1 = Account(1000, 263744941050)

print(f"User balance: {acc1.bal}, Account number: {acc1.account_id}")

acc1.credit(500)
acc1.debit(1000)
acc1.total()