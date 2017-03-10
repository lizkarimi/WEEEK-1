class BankAccount(object):
  
  def withdraw(self):
    pass
  def deposit(self):
    pass
  
class SavingsAccount(BankAccount): #inheritance, Savings account inheriting from BankAccount
  def __init__(self):
    self.balance = 500

    """deposit method from BankAccount is implemented in the savings 
    account to depict Abstraction/encapsulation"""
  def deposit(self, amount):
    if amount <= 0:
      return "Invalid deposit amount"
    else:
      self.balance = self.balance + amount
    return self.balance
  
  def withdraw(self, amount):
    if self.balance - amount < 500:
      return 'Cannot withdraw beyond the minimum account balance'
    elif amount >= self.balance:
      return 'Cannot withdraw beyond the current account balance'
    elif amount < 0:
      return 'Invalid withdraw amount'
    else :
      self.balance = self.balance - amount
      return self.balance
      
class CurrentAccount(BankAccount):
  def __init__(self): 
    self.balance = 0
    
  def deposit(self, amount):
    if amount < 0:
      return 'Invalid deposit amount'
    else:
      self.balance = self.balance + amount
      return self.balance
      
  def withdraw(self, amount):
    if amount < 0:
      return 'Invalid withdraw amount'
    elif amount > self.balance:
      return 'Cannot withdraw beyond the current account balance'
    else:
      self.balance = self.balance - amount
      return self.balance
