#Imports
import os
import threading
import random
from PIL import Image
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
from datetime import datetime

#Variables
assets_path = os.path.join(os.path.dirname(__file__), "Assets") #sets the folder where assets are stored
mode = 'regular' #variable for what mode in
page = 1 #varibale for page
last_page = False #check varible if the page is the last one
user = 'a' #check variable to make sure the user does not submit the old user
force_reset_count = int(0) #variabale to count how many times the reset button has been pressed
close_count = int(0) #variabale to count how many times the close button has been pressed
userdict = { #dictonary to alocate user to a number
    1 : 'user 1',
    2 : 'user 2',
    3 : 'user 3',
    4 : 'user 4',
    5 : 'user 5',
    6 : 'user 6',
    7 : 'user 7',
    8 : 'user 8',
    9 : 'user 9',
}

def image_format(deck, image):#formats image to correct requirements
    key_image = PILHelper.create_image(deck)
    key_image.paste(image)
    return PILHelper.to_native_format(deck, key_image)

def gen_time(): #returns curent time in 24 hour time but without leading zeros. If you want to test the time abilites comment out the first 2 lines and un comment the third line
    current_time = datetime.now()
    current_time = int(str(current_time.hour) + str(current_time.minute))
    #time = int(input("What the time? "))
    return current_time

def BLD_check(type):
    if type == 'read':#reads the file for the last user who did the task
        with open(f'Assets/BLD.txt', 'rb') as f:#gets the last line of the BLD file
            try:  # catch OSError in case of a one line file
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            BLD = f.readline().decode()
        f.close()
    if type == 'add':#updates the BLD
        with open(f'Assets/BLD.txt', 'rb') as f:#gets current BLD
            try:  # catch OSError in case of a one line file
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            BLD = f.readline().decode()
        f.close()
        current_time = gen_time()#calculates current time
        if BLD[0] == 'W':#checks if breakfast is waiting
            if current_time >= 915 and current_time <= 945:#if pressed on time, saves as on time
                BLD = 'T' + BLD[1] + BLD[2]
            else:#saves as not on time
                BLD = 'X' + BLD[1] + BLD[2]
        elif BLD[1] == 'W':#checks for lunch and does as above
            if current_time >= 1715 and current_time <= 1545:
                BLD = BLD[0] + 'T' + BLD[2]
            else:
                BLD = BLD[0] + 'X' + BLD[2]
        elif BLD[2] == 'W':#checks for dinner and does as above
            if current_time >= 2115 and current_time <= 2145:
                BLD = BLD[0] + BLD[1] + 'T'
            else:
                BLD = BLD[0] + BLD[1] + 'X'
        f = open(f'Assets/BLD.txt', "a")#save to file
        f.write(f'\n{BLD}')
        f.close
    return BLD #returns the BLD

def load_page(page):
    global last_page, user
    try:
        if int(page) ==  1:#if on the first page
            if user[-1] == '1':#checks if the user is selected, loads slelected image
                deck.set_key_image(0, image_format(deck,Image.open(os.path.join(assets_path, f"selectedpfp/pfp_{int(user[-1])-1}.jpg")).convert("RGBA")))
            else:#if the user is not selected, loads regular image
                deck.set_key_image(0, image_format(deck,Image.open(os.path.join(assets_path, f"unselectedpfp/pfp_0.jpg")).convert("RGBA")))
        else:#if not the first page, loads the back image
            deck.set_key_image(0, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/back.jpg")).convert("RGBA")))
        last_page = False #sets page to not last
    except:#if no images exist, page is last and loads icon as last
        deck.set_key_image(1, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/end.jpg")).convert("RGBA")))
        last_page = True

    try:
        if str((3 * page) - 1) != user[-1]:#checks if the user is selected, loads slelected image
            deck.set_key_image(1, image_format(deck,Image.open(os.path.join(assets_path, f"unselectedpfp/pfp_{(3 * page) - 2}.jpg")).convert("RGBA")))
        else:#if the user is not selected, loads regular image
            deck.set_key_image(1, image_format(deck,Image.open(os.path.join(assets_path, f"selectedpfp/pfp_{int(user[-1])-1}.jpg")).convert("RGBA")))
        last_page = False #sets page to not last
    except:#if no images exist, page is last and loads icon as last
        deck.set_key_image(1, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/end.jpg")).convert("RGBA")))
        last_page = True
   
    try:
        if str(3 * page) == user[-1]: #checks if the user is selected, loads slelected image
            deck.set_key_image(2, image_format(deck,Image.open(os.path.join(assets_path, f"selectedpfp/pfp_{int(user[-1])-1}.jpg")).convert("RGBA")))
        else: #if the user is not selected, loads regular image
            deck.set_key_image(2, image_format(deck,Image.open(os.path.join(assets_path, f"unselectedpfp/pfp_{(3 * page) - 1}.jpg")).convert("RGBA")))
        last_page = False #sets page to not last
    except:#if no images exist, page is last and loads icon as last
        deck.set_key_image(2, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/end.jpg")).convert("RGBA")))
        last_page = True
    
    try:
        if str(3 * page + 1) == user[-1]: #checks if the user is selected, loads slelected image
            deck.set_key_image(3, image_format(deck,Image.open(os.path.join(assets_path, f"selectedpfp/pfp_{(3 * page)}.jpg")).convert("RGBA")))
        else: #if the user is not selected, loads regular image
            deck.set_key_image(3, image_format(deck,Image.open(os.path.join(assets_path, f"unselectedpfp/pfp_{(3 * page)}.jpg")).convert("RGBA")))
        last_page = False #sets page to not last
    except:#if no images exist, page is last and loads icon as last
        deck.set_key_image(3, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/end.jpg")).convert("RGBA")))
        last_page = True

    if last_page == False:#if not last page, sets icon to next
        deck.set_key_image(4, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/next.jpg")).convert("RGBA")))
    else: # if last page sets to end
        deck.set_key_image(4, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/end.jpg")).convert("RGBA")))

def key_press(deck, key, state):
    global mode, page, last_page, user, force_reset_count, close_count #global variables
    # Use a scoped-with on the deck to ensure we're the only thread using it right now.
    with deck:
        if mode == "regular" and state == True: #checks that is on the home screen
            for count in range(deck.key_count()):#prevents multiple presses occuring in 1 tap
                if key == 3 and key == count:#if key is task done
                    for k in range(5):
                        # Draw the individual key images to each of the keys.
                        if  k != 4 and k != 5:
                            deck.set_key_image(k, image_format(deck,Image.open(os.path.join(assets_path, f"unselectedpfp/pfp_{k}.jpg")).convert("RGBA")))
                    deck.set_key_image(4, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/next.jpg")).convert("RGBA")))#makes the next and save icons
                    deck.set_key_image(5, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/save.jpg")).convert("RGBA")))
                    page = 1 #resets page to 1
                    last_page = False # resets to last page false
                    close_count = int(0) # resets close counter
                    force_reset_count = int(0) # resets bld reset counter
                    mode = 'task_done'# sets mode to task done
                elif key == 1 and key == count or key == 2 and key == count or key == 4 and key == count: #if any blank buttons are pressed resets counters
                    force_reset_count = int(0)
                    close_count = int(0)
                elif key == 5 and key == count:# if key is BLD image
                    force_reset_count = force_reset_count + int(1) # adds to reset counter
                    if force_reset_count == int(3):#if count is pressed 3 times, resets the image
                        f = open(f'Assets/BLD.txt', "a")
                        f.write(f'\nWWW')
                        f.close
                        deck.set_key_image(5, image_format(deck,Image.open(os.path.join(assets_path, f"Codes/WWW.jpg")).convert("RGBA")))
                        force_reset_count = int(0) # resets bld reset counter
                    close_count = int(0) # resets close counter
                elif key == 0 and key == count:# if key is exit
                    force_reset_count = int(0)# resets bld reset counter
                    close_count = close_count + int(1) 
                    if close_count == int(3):#if count is pressed 3 times, closes app
                        deck.reset()# Reset deck, clearing all button images.
                        # Close deck handle, terminating internal worker threads.
                        deck.close()
        elif mode == "task_done" and state == True: #when task_done mode is chosen
            for count in range(deck.key_count()):#prevents multiple presses occuring in 1 tap
                if key == 0 and count == 0 and page != 1:#if back button pressed, loads previous page
                    page = page - 1
                    load_page(page)
                elif key == count and key != 4 and key != 5 and last_page == False or last_page == True and key == count and key != 3 and key != 4 and key != 5: # when a user input made sets the seleccted user as the one chosen on the board
                    if user == userdict[page * 3 - 2 + key]:# unselects the user if pressed a second time
                        user = 'a'
                    else:
                        user = userdict[page * 3 - 2 + key] # if pressed for the first time, sets the user
                    load_page(page)#resets all images
                elif count == 4 and key == 4 and last_page == False: #Loads next page
                    page = page + 1
                    load_page(page)#resets all images
                elif count == 5 and key == 5:
                    if user != 'a':#ensures that it is a new user and not the old one
                        f = open(f"Assets/Task_done.txt", "a") #saves user to permanent file
                        f.write(f'\n{user[-1]}')
                        f.close()
                        BLD_check('add')#updates the BLD icon 
                    with open(f'Assets/Task_done.txt', 'rb') as f: #get last user saved
                        try:  # catch OSError in case of a one line file
                            f.seek(-2, os.SEEK_END)
                            while f.read(1) != b'\n':
                                f.seek(-2, os.SEEK_CUR)
                        except OSError:
                            f.seek(0)
                        last_user = f.readline().decode()
                    f.close()
                    random_number = random.randint(1,2) #randomly choses if the close icon or end icon is used
                    if random_number == 1:
                        deck.set_key_image(0, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/end.jpg")).convert("RGBA")))
                    else:
                        deck.set_key_image(0, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/close.jpg")).convert("RGBA")))
                    #loads rest of homescreen
                    deck.set_key_image(1, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/Last_done.jpg")).convert("RGBA")))
                    deck.set_key_image(2, image_format(deck,Image.open(os.path.join(assets_path, f"unselectedpfp/pfp_{int(last_user)-1}.jpg")).convert("RGBA")))
                    deck.set_key_image(3, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/task_done.jpg")).convert("RGBA")))
                    deck.set_key_image(4, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/BLD.jpg")).convert("RGBA")))
                    deck.set_key_image(5, image_format(deck,Image.open(os.path.join(assets_path, f"Codes/{BLD_check('read')}.jpg")).convert("RGBA")))
                    user = 'a'# resets user to hold variable
                    mode = 'regular'#sets mode back to regualar

if __name__ == "__main__":
    streamdeck = DeviceManager().enumerate()#gets the streamdeck
    for index, deck in enumerate(streamdeck):
        deck.open()# turns on deck
        deck.reset()# Reset deck, clearing all button images.
        deck.set_brightness(30) # Set initial screen brightness to 30%.
        with open(f'Assets/Task_done.txt', 'rb') as f: #get last user saved
            try:  # catch OSError in case of a one line file
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            last_user = f.readline().decode()
        f.close()
        current_time = gen_time() # generates time
        if current_time >= 2300 and current_time <= 800:# resets the BLD icon if day has not started
            f = open(f"Assets/BLD.txt", "a")
            f.write(f'\nWWW')
            f.close()
        with deck: # Use a scoped-with on the deck to ensure we're the only thread using it right now.
            random_number = random.randint(1,2)#randomly choses if the close icon or end icon is used
            if random_number == 1:
                deck.set_key_image(0, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/end.jpg")).convert("RGBA")))
            else:
                deck.set_key_image(0, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/close.jpg")).convert("RGBA")))
            #loads rest of homescreen
            deck.set_key_image(1, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/Last_done.jpg")).convert("RGBA")))
            deck.set_key_image(2, image_format(deck,Image.open(os.path.join(assets_path, f"unselectedpfp/pfp_{int(last_user)-1}.jpg")).convert("RGBA")))
            deck.set_key_image(3, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/task_done.jpg")).convert("RGBA")))
            deck.set_key_image(4, image_format(deck,Image.open(os.path.join(assets_path, f"ICON/BLD.jpg")).convert("RGBA")))
            deck.set_key_image(5, image_format(deck,Image.open(os.path.join(assets_path, f"Codes/{BLD_check('read')}.jpg")).convert("RGBA")))
        deck.set_key_callback(key_press)# Register callback function for when a key state changes.
        for t in threading.enumerate():# Wait until all application threads have terminated
            try:
                t.join()
            except RuntimeError:
                pass