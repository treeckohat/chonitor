#Everything not marked as Ethan is Leon
import readWriteData #createUserList and writeTotxtFile 
from datetime import datetime #date on receipt
import string #formatting user input
import time

class userHandle: #creates the class which handles all the user's variables
  def __init__(self, userList, user): # loads in user from database
    self.user = user
    self.userList = userList
    self.pin = userList[user][0]
    self.bal = float(userList[user][1])
    self.prevdeposit = int(userList[user][2])
    self.prevwithdrawal = int(userList[user][3])

  def changePIN(self): # function to change pin
    userCheck = input('Current pin: ')
    if userCheck != self.pin:
      input("Incorrect pin. Press enter to return to menu.")
      return False
    while True:
      newPin = input("New pin (4 digit pin) (enter 'x' to cancel): ")
      if newPin.lower() == 'x': # quits function (Ethan)
        print('Exiting')
        time.sleep(1)
        return False
      confirmPin = input('Confirm new pin: ')
      if newPin.isnumeric() == True and len(newPin) == 4 and newPin == confirmPin: # checks all pin parameters are met, then saves them to class
        self.pin = newPin
        input("PIN saved. Press enter to return to menu.")
        return True
      elif newPin != confirmPin: # if pin confirmation was inputted incorrectly
        input('PIN does not match.')
      else:
        input("PIN can only be 4 digit, numerical (e.g. '1234').") # bad input
    
  def save(self): #saves user info back to the text file, encrypted
    self.userList[self.user] = [self.pin, str(self.bal), str(self.prevdeposit), str(self.prevwithdrawal)]
    readWriteData.writeTotxtFile(self.userList)
  
  def history(self): #gives history of previous transactions, if in database.
    print('Previous transactions (will be 0 if you have not made one): ')
    print(f'Last deposit: \n${self.prevdeposit}')
    input(f'Last withdrawal: \n${self.prevwithdrawal}\n')
  
  def deposit(self):
    print("Enter 'x' to go back")
    while True:
      try:
        amount = input("Deposit Amount: ")
        if amount.lower() == 'x':# quits function (Ethan)
          print('Exiting')
          time.sleep(1)
          return 'x'
        amount = int(amount.translate(str.maketrans('', '', string.punctuation))) #tries to convert string into an integer
        if amount > 10000:
          print("enter an amount less that $10000.")
        elif amount <= 10000: 
          confirmation = input(f'enter (Y) to confirm. Anything else to cancel. (depositing ${amount})\n').lower()
          if confirmation == 'y': #asks for a confirmation
            self.bal = self.bal + amount # updates balance
            self.prevdeposit = amount #updates history
            return amount
        else:
          input("Transaction cancelled. Press enter to return to menu.")
          return False
      except: #if string cannot be made a integer, return error
        print("Sorry, please input a valid amount.")        
    
  def withdraw(self):
    print("Enter 'x' to go back")
    while True:
      try:
        amount = input("Withdrawal Amount (in banknotes, no coins): ")
        if amount.lower() == 'x':# quits function (Ethan)
          print('Exiting')
          time.sleep(1)
          return 'x'
        amount = int(amount.translate(str.maketrans('', '', string.punctuation)))
        if amount > 10000:
          print("enter an amount less that $10000.")
        elif amount%5 == 0 and self.bal >= amount: #checks if can be withdrawed with notes and enough credit
          confirmation = input(f'enter (Y) to confirm. Anything else to cancel. (withdrawing ${amount})\n').lower()
          if confirmation == 'y': #asks for a confirmation
            self.bal = self.bal - amount #updates balance
            self.prevwithdrawal = amount #updates history
            return amount
          else:
            input("Transaction cancelled. Press enter to return to menu.")
            return False
        elif self.bal < amount:
          input("Not enough balance to withdraw. Press enter to return to menu.")
          return False
        else:
          print("We only do banknotes. Please input a valid amount.")
      except: #if string cannot be made an integer, return error
        print("Sorry, please input a valid amount.")
        
  def printReceipt(self, amount, transactionType):
    now = datetime.now() # gets date and time of transaction
    transactionTime = now.strftime('%H:%M:%S')
    transactionDate = now.strftime('%d/%m/%Y')
    lines = ['\tMORA BANK', 'Date:\t' + transactionDate, 'Time:\t' + transactionTime, 'User:\t' + self.user, 'Transaction:\t' + transactionType , 'Amount:\t$' + str(amount), 'Available Balance:\t$' + str(self.bal)]
    #creates a list of lines needed to be printed onto the receipt
    with open('receipt.txt', 'w') as receipt: #writes onto receipt.txt
      for line in lines:
        receipt.write(line)
        receipt.write('\n')
      receipt.close()