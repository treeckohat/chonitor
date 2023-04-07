from tkinter import Menu
import win32gui
import time
import os
import readWriteData
import functions

def clear(): #function to clear the screen by trying to clean screen on windows
    try:
        os.system("cls")
    except:
        pass

def open():
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
          .&&&&/              *&&&&&&&&&&&.#&&&&&&&             &&&&&&&%.&&&&&&&&&&&/              (&&&&
          .&&&&/            /&&&&&&&&&/     %&&&&&&&&         &&&&&&&&&     *&&&&&&&&&(            (&&&&
           &&&&%          .&&&&&&&@#         #&&&&&&&&,     ,&&&&&&&&%         (&&&&&&&&.          &&&&&
           &&&&&         %&&&&&&&*            ,&&&&&&&&&.  &&&&&&&&&,            ,&&&&&&&%         &&&&&
           *&&&&/       &&&&&&&#                %&&&&&&&&&&&&&&&&&&                (&&&&&&&       (&&&&,
            &&&&&      @&&&&&&.                   &&&&&&&&&&&&&&&                    &&&&&&&      &&&&&
             &&&&&    %&&&&&&                     %&&&&&&&&&&&&&%                     &&&&&&&    @&&&&
             .&&&&&  .&&&&&&.               /&&&&&&&&&&&&&&&&&&&&&&&&&/                &&&&&&,  &&&&&
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
    action = input(
    """To login type 1                                                                          To sign up type 2
""")
    while action != "1" and action != "2":
        print("Not a valid input, Try again")
        action = input(
    """To login type 1                                                                          To sign up type 2
""")
    return action

def login():
    while True:
        print(user_list)
        user = input("User: ")
        while user not in user_list:
            print("User not in database, please type a valid user.")
            user = input("User: ")
        check_pin = user_list[user][0]
        pin = input("Pin: ")
        while len(pin) != 4 or pin.isdigit() == False:
            print("Not a valid PIN, Try again")
            pin = input("Pin: ")
        if pin == check_pin:
            return user
        else:
            clear()
            print("Incorrect user or PIN, Try again")
            print('If you have forgotten your user or PIN contact your account provider at 911')

def sign_up():
    user = input("User: ")
    while user == "":
        print("Field must not be blank.")
        user = input("User: ")
    while user in user_list:
        print("This username has been taken already please choose a new one")
        user = input("User: ")
    pin = input("Pin: ")
    while pin == "":
        print("Field must not be blank.")
        pin = input("Pin: ")
    while len(pin) != 4 or pin.isdigit == 'False':
        print("Not a valid PIN, Try again")
        pin = input("Pin: ")
    user_list[user] = [pin, "0", "0", "0"]
    readWriteData.writeTotxtFile(user_list)
    return user

hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 0, 0, 1100, 800, True)
user_list = readWriteData.createUserList()

action = open()
clear()
print("press escape to go back")
if action == "1":
    state = "login"
    user = login()
if action == "2":
    state = "sign up"
    user = sign_up()
functions.userSession().startUser(user_list, user)
time.sleep(10)

clear()
print(f"Welcome {user}")

menu = "true"
while menu == "true":
    clear()
    print('''Menu
1 - Deposit
2 - Withdraw
3 - Past transactions
4 - Change PIN
5 - Logout
''')
    action = input('What would you like to do: ')
    if action == '1':
        functions.userSession().deposit()
    elif action == '2':
        functions.userSession().withdraw()
    elif action == '3':
        functions.userSession().history()
    elif action == '4':
        functions.userSession().changePIN()
    elif action == '5':
        menu = 'false'
    else:
        print('Not a valid input, Please try again.')
        time.sleep(1)
readWriteData.writeTotxtFile(user_list)
quit()
