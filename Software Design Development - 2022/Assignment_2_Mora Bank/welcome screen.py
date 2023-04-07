import win32gui #To reposition and shape the window
import time # to create breaks in code
import os # to clear screen
import readWriteData #createUserList and writeTotxtFile 
from functions import * #change pin, save, deposit, withdrawal, and receipt
import re # check characters

def clear(): #function to clear the screen by trying to clean screen on windows (Ethan)
    try:
        os.system("cls")
    except:
        pass

def open(): #opening screen and leads to login, sign up or exit (Ethan)
    print(
"""

 __          __  _                            _______      __  __                   ____              _    
 \ \        / / | |                          |__   __|    |  \/  |                 |  _ \            | |   
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___   | \  / | ___  _ __ __ _  | |_) | __ _ _ __ | | __
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \  | |\/| |/ _ \| '__/ _` | |  _ < / _` | '_ \| |/ /
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) | | |  | | (_) | | | (_| | | |_) | (_| | | | |   < 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/  |_|  |_|\___/|_|  \__,_| |____/ \__,_|_| |_|_|\_\ 


                                                *#&&&&&&&&&&&&&@&#*                                                
                                       .#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(
                                  .&&&&&&&&&&&&%/      /&&&(     ./&@&&&&&&&&&&&.
                              .&&&&&&&&&(           ,&&&&&&&&&*           #&&&&&&&&&.
                           *&&&&&&&%              #&&&&&&&&&&&&&%              &&&&&&&&*
                        .&&&&&&&.               (&&&&&&&& %&&&&&&&%               ,&&&&&&&.
                      #&&&&&&.                 &&&&&&&&     %&&&&&&&.                .@&&&&&(
                    #&&&&&#                  (&&&&&&&         @&&&&&&#                  %&&&&&(
                  *&&&&&/                   #&&&&&&&           &&&&&&&%                   (&&&&&,
                 &&&&&%                    (&&&&&&&             &&&&&&&#                    &&&&&&
               ,&&&&&                      &&&&&&&               &&&&&&&.                     &&&&&.
              (&&&&&                      &&&&&&&(               /&&&&&&&                      &&&&&/
             (&&&&#                       &&&&&&&.                &&&&&&&                       %&&&&/
            ,&&&&%                       .&&&&&&&                 &&&&&&&,                       &&&&&.
            &&&&&                        .&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,                        &&&&&
           (&&&&.                       #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%                       *&&&&/
           &&&&&                    %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                    @&&&&
           &&&&#                 &&&&&&&&&&&&&&&&&               &&&&&&&&&&&&&&&&&                 %&&&&
          .&&&&/              *&&&&&&&&&&&.#&&&&&&&             &&&&&&&%.&&&&&&&&&&&\              (&&&&
          .&&&&/            /&&&&&&&&&/     %&&&&&&&&         &&&&&&&&&     *&&&&&&&&&(            (&&&&
           &&&&%          .&&&&&&&@#         #&&&&&&&&,     ,&&&&&&&&%         (&&&&&&&&.          &&&&&
           &&&&&         %&&&&&&&*            ,&&&&&&&&&.  &&&&&&&&&,            ,&&&&&&&%         &&&&&
           *&&&&/       &&&&&&&#                %&&&&&&&&&&&&&&&&&&                (&&&&&&&       (&&&&,
            &&&&&      @&&&&&&.                   &&&&&&&&&&&&&&&                    &&&&&&&      &&&&&
             &&&&&    %&&&&&&                     %&&&&&&&&&&&&&%                     &&&&&&&    @&&&&
             .&&&&&  .&&&&&&.               /&&&&&&&&&&&&&&&&&&&&&&&&&\                &&&&&&,  &&&&&
              .&&&&& %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&* *&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& &&&&&
                &&&&&(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#           #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&
                 %&&&&@      /%&&&&&&&&@&&&#,                         ,#&&&&&&&&&&&@%(.     &&&&&#
                   &&&&&&                                                                 &&&&&&
                    .&&&&&&.                                                           .&&&&&&
                       &&&&&&%                                                       &&&&&&&
                         (&&&&&&&                                                 &&&&&&&/
                            #&&&&&&&%                                        .&&&&&&&&#
                               ,&&&&&&&&&&,                             ,&&&&&&&&&&.
                                   .%&&&&&&&&&&&&&%(*..     ..*(%&&&&&&&&&&&&&%
                                         ,&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%,
                                                   .*/(#####(/*.                                          """)
    time.sleep(.25)
    print("Enter 'x' to quit program")
    action = input(
    """To login type 1                                                                          To sign up type 2
""")
    while action != "1" and action != "2":#check to make sure input is valid
        if action.lower() == 'x': #ends code if user is done
            quit()#ends program
        print("Not a valid input, Try again")
        action = input(
    """To login type 1                                                                          To sign up type 2
""")
    return action #gives back the choice

def login(): #(Ethan)
    while True:
        print("Enter 'x' to go back")
        user = input("User: ") #asks user for their user
        if user.lower() == 'x': #goes back to opening page
            print('Exiting')
            time.sleep(1)
            return 'x'
        while user not in user_list: #checks to see if the user is real. if it is not keep
            print("User not in database, please type a valid user.")
            user = input("User: ")
            if user.lower() == 'x': #goes back to opening page
                print('Exiting')
                time.sleep(1)
                return 'x'
        check_pin = user_list[user][0]#creates the correct pin to check against the input pin
        pin = input("Pin: ")
        if pin.lower() == 'x': #goes back to opening page
            print('Exiting')
            time.sleep(1)
            return 'x'
        elif pin == check_pin:#if the pin is the same then the user is returned
            return user
        else: #if the pin is not the smae it asks for a new user or pin
            clear()
            print("Incorrect user or PIN, Try again. If you have forgotten your user or PIN contact your account provider at 911 ")

def sign_up(): #(Ethan)
    print("Enter 'x' to go back")
    user = input("User(Only letters and numbers): ")
    if user.lower() == 'x': #goes back to opening page
        print('Exiting')
        time.sleep(1)
        return 'x'
    while(not re.match("^[A-Za-z0-9]*$", user)): # checks that the user only contains letters and numbers
        print('User can only contain letters or numbers)')
        user = input("User: ")
    while user == "": #makes sure that there is an input
        print("Field must not be blank.")
        user = input("User: ")
    while user in user_list: # checks to see if a user has already been taken
        print("This username has been taken already please choose a new one")
        user = input("User: ")
    pin = input("Pin: ")
    if pin.lower() == 'x': #goes back to opening page
        print('Exiting')
        time.sleep(1)
        return 'x'
    while pin == "": #makes sure that there is an input
        print("Field must not be blank.")
        pin = input("Pin: ")
    while len(pin) != 4 or pin.isdigit() == 'False': #Checks if the pin is 4 digits and a number
        print("Not a valid PIN, Try again")
        pin = input("Pin: ")
    user_list[user] = [pin, "0", "0", "0"] # adds the user to the user list
    readWriteData.writeTotxtFile(user_list) #adds the updated user list to the text file and saves it
    return user

hwnd = win32gui.GetForegroundWindow() #Sets the size and position of the window(Ethan)
win32gui.MoveWindow(hwnd, 0, 0, 1100, 800, True)

user_list = readWriteData.createUserList() #downloads the user list from the encrypted text file

action = open() #Starts the opening and gets the action of the user
clear()
if action == "1": #Starts login if chosen(Ethan)
    user = login()
if action == "2": #Starts sign up if chosen
    user = sign_up()
while user == 'x': #if the user has chosen to go back, restarts the menu untill they make a new choiceto either login, sign up or quit(Ethan)
        clear()
        action = open()
        clear()
        if action == "1":
            user = login()
        if action == "2":
            user = sign_up()

userSession = userHandle(user_list, user) #'boots up' the user (Leon)
clear()
print(f"Welcome {user}")
menu = "true"
while menu == "true": #(Ethan)
    print(f'''Menu

Balance ${user_list[user][1]}

1 - Deposit
2 - Withdraw
3 - Past transactions
4 - Change PIN
5 - Return card
''')
    action = input('What would you like to do: ') #gets the users next action
    while action == '1':#(Leon)
        transactionChecker = userSession.deposit()
        if transactionChecker == 'x':
            action = 'x'
        elif transactionChecker != False: #this checks whether a change has been made, then prints a receipt and saves to database accordingly
            userSession.printReceipt(transactionChecker, 'deposit')  
            userSession.save()
            input("Transaction complete, receipt has been printed. Press enter to return to menu.")
        action = 'x'
    while action == '2':#(Leon)
        transactionChecker = userSession.withdraw()
        if transactionChecker == 'x':
            action = 'x'
        elif transactionChecker != False: #ditto
            userSession.printReceipt(transactionChecker, 'withdrawal')  
            userSession.save()
            input("Transaction complete, receipt has been printed. Press enter to return to menu.")
        action = 'x'
    while action == '3':#(Leon)
        userSession.history()
        action = 'x'
    while action == '4': #(Leon)
        changedChecker = userSession.changePIN()
        if changedChecker == True: #ditto but checks pin change to avoid unnecessary writing to txt file (which i think requires more processing than an if loop)
          userSession.save()
        action = 'x'
    while action == '5': #restarts at the opening to get a new user(Ethan)
        action = open() #Starts the opening and gets the action of the user
        clear()
        if action == "1": #Starts login if chosen(Ethan)
            user = login()
        if action == "2": #Starts sign up if chosen
            user = sign_up()
        while user == 'x': #if the user has chosen to go back, restarts the menu untill they make a new choiceto either login, sign up or quit(Ethan)
                clear()
                action = open()
                clear()
                if action == "1":
                    user = login()
                if action == "2":
                    user = sign_up()
        userSession = userHandle(user_list, user) #'boots up' the user
        clear()
        action = 'x'
        print(f"Welcome {user}")
    if action == 'x': #alows the user to pass through and gets the users new action
        pass
    else:
        print('Not a valid input, Please try again.')
        time.sleep(1)
    clear()
readWriteData.writeTotxtFile(user_list)
quit()