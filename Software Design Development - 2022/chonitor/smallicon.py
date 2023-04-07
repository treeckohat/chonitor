import os
import threading
import sqlite3
from PIL import Image, ImageOps
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper

mode = 'regular'
toggle = False
page = 1
last = False
selected0 = False
selected1 = False
selected2 = False
selected3 = False
selected4 = False
selected5 = False
selected6 = False


ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    uid number,
                    name text, 
                    email text, 
                    contact number,
                    password text,
                    last_time1 number,
                    average_time1 number,
                    total_time1 number,
                    last_time2 number,
                    average_time2 number,
                    total_time2 number,
                    last_time3 number,
                    average_time3 number,
                    total_time3 number
                )
            ''')
con.commit()

def image_format(deck, image):
    key_image = PILHelper.create_image(deck)
    key_image.paste(image)

    return PILHelper.to_native_format(deck, key_image)

def gen_uid():
    uid = 0
    for row in con.execute("Select * from record"):
        uid = uid + 1
    return uid

def change_page(page):
    global last
    try:
        deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{(3 * page) - 1}.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\next.jpg")).convert("RGBA")))
        last = False
    except:
        deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\end.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\end.jpg")).convert("RGBA")))
        last = True
    
    try:
        deck.set_key_image(2, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{(3 * page)}.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\next.jpg")).convert("RGBA")))
        last = False
    except:
        deck.set_key_image(2, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\end.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\end.jpg")).convert("RGBA")))
        last = True

    try:
        deck.set_key_image(3, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{(3 * page) + 1}.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\next.jpg")).convert("RGBA")))
        last = False
    except:
        deck.set_key_image(3, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\end.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\end.jpg")).convert("RGBA")))
        last = True
    
    if last == False:
        try:
            check1 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{(3 * page + 3)}.jpg")).convert("RGBA"))
        except:
            try:
                check2 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{(3 * page + 2)}.jpg")).convert("RGBA"))
                deck.set_key_image(int(deck.key_count())-int(2), check2)
            except:
                deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\end.jpg")).convert("RGBA")))
            last = True

    print(f'page changed to {page}')

def key_press(deck, key, state):
    # Use a scoped-with on the deck to ensure we're the only thread using it right now.
    global toggle, mode, page, last
    with deck:
        if mode == "regular" and state == True:
            if key == 0 :
                print('task done')
                for k in range(deck.key_count()):
                    # Draw the individual key images to each of the keys.
                    if  k != int(deck.key_count())-int(2) and k != int(deck.key_count())-int(1):
                        deck.set_key_image(k, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{k}.jpg")).convert("RGBA")))
                deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\next.jpg")).convert("RGBA")))
                deck.set_key_image(int(deck.key_count())-int(1), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\close.jpg")).convert("RGBA")))
                page = 1
                last = False
                mode = 'task_done'
            elif key == 1:
                print('help')
                for k in range(deck.key_count()):
                    # Draw the individual key images to each of the keys.
                    if  k != int(deck.key_count())-int(2) and k != int(deck.key_count())-int(1):
                        deck.set_key_image(k, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{k}.jpg")).convert("RGBA")))
                deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\next.jpg")).convert("RGBA")))
                deck.set_key_image(int(deck.key_count())-int(1), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\close.jpg")).convert("RGBA")))
                page = 1
                last = False
                mode = "help"
            elif key == 2 and toggle == False:
                print('anya is a cat')
                deck.set_key_image(key, image_format(deck,Image.open(os.path.join(ASSETS_PATH, "unselectedpfp\\pfp_10.jpg")).convert("RGBA")))
                toggle = True
            elif key == 2 and toggle == True:
                print('anya is back')
                deck.set_key_image(key, image_format(deck,Image.open(os.path.join(ASSETS_PATH, "unselectedpfp\\pfp_2.jpg")).convert("RGBA")))
                toggle = False
            elif key == 3:
                uid = 1
                con = sqlite3.connect('userdata.db')
                for row in con.execute("Select * from record"):
                    uid = uid + 1
                print(f'added uid {uid}')
                cur = con.cursor()
                cur.execute("INSERT INTO record VALUES (:uid, :name, :email, :contact, :password, :last_time1, :average_time1, :total_time1, :last_time2, :average_time2, :total_time2, :last_time3, :average_time3, :total_time3)", {
                                'uid': str(uid),
                                'name': 'test',
                                'email': 'e@email.com',
                                'contact': '421',
                                'password': 'pass',
                                'last_time1': '1',
                                'average_time1': '1',
                                'total_time1': '1',
                                'last_time2': '2',
                                'average_time2': '2',
                                'total_time2': '2',
                                'last_time3': '3',
                                'average_time3': '3',
                                'total_time3': '3'
                                })
                con.commit()
            elif key == 4:
                sql = ''' UPDATE record
                SET email = ?
                WHERE uid = ?'''
                uid = 0
                con = sqlite3.connect('userdata.db')
                for row in con.execute("Select * from record"):
                    uid = uid + 1
                cur = con.cursor()
                cur.execute(sql,("e@gmail.com", uid))
                con.commit()
                print("changed value")
            elif key == int(deck.key_count())-int(1):
                # Reset deck, clearing all button images.
                deck.reset()
                # Close deck handle, terminating internal worker threads.
                deck.close()
        elif mode == "help" and state == True:
            for count in range(deck.key_count()):
                if key == 0 and count == 0 and page != 1:
                    print('back')
                    change_page(page-1)
                    if (int(page) - 1) ==  1:
                        deck.set_key_image(0, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_0.jpg")).convert("RGBA")))
                    page = page - 1
                elif key == count and key != int(deck.key_count())-int(2) and key != int(deck.key_count())-int(1):
                    print(f'get help from {page * 3 - 2 + key}')
                elif key == count and key == int(deck.key_count())-int(2) and key != int(deck.key_count())-int(1) and last == True:
                    print(f'get help from {page * 3 - 2 + key}')
                elif count == int(deck.key_count())-int(2) and key == int(deck.key_count())-int(2) and last == False:
                    print('next')
                    page = page + 1
                    change_page(page)
                    deck.set_key_image(0, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\back.jpg")).convert("RGBA")))
                elif count == int(deck.key_count())-int(1) and key == int(deck.key_count())-int(1):
                    for k in range(deck.key_count()):
                        # Draw the individual key images to each of the keys.
                        if k != 0 and k != 1 and k != int(deck.key_count())-int(1):
                            deck.set_key_image(k, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{k}.jpg")).convert("RGBA")))
                    deck.set_key_image(0, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\task_done.jpg")).convert("RGBA")))
                    deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\help.jpg")).convert("RGBA")))
                    deck.set_key_image(int(deck.key_count())-int(1), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\close.jpg")).convert("RGBA")))
                    mode = 'regular'
        elif mode == "task_done" and state == True:
            for count in range(deck.key_count()):
                if key == 0 and count == 0 and page != 1:
                    print('back')
                    change_page(page-1)
                    if (int(page) - 1) ==  1:
                        deck.set_key_image(0, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_0.jpg")).convert("RGBA")))
                    page = page - 1
                elif key == count and key != int(deck.key_count())-int(2) and key != int(deck.key_count())-int(1):
                    print(f'{page * 3 - 2 + key} did a task')
                elif key == count and key == int(deck.key_count())-int(2) and key != int(deck.key_count())-int(1) and last == True:
                    print(f'{page * 3 - 2 + key} did a task')
                elif count == int(deck.key_count())-int(2) and key == int(deck.key_count())-int(2) and last == False:
                    print('next')
                    page = page + 1
                    change_page(page)
                    deck.set_key_image(0, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\back.jpg")).convert("RGBA")))
                elif count == int(deck.key_count())-int(1) and key == int(deck.key_count())-int(1):
                    for k in range(deck.key_count()):
                        # Draw the individual key images to each of the keys.
                        if k != 0 and k != 1 and k != int(deck.key_count())-int(1):
                            deck.set_key_image(k, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{k}.jpg")).convert("RGBA")))
                    deck.set_key_image(0, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\task_done.jpg")).convert("RGBA")))
                    deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\help.jpg")).convert("RGBA")))
                    deck.set_key_image(int(deck.key_count())-int(1), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\close.jpg")).convert("RGBA")))
                    mode = 'regular'




if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()
    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        # Set initial screen brightness to 30%.
        deck.set_brightness(30)

        # Use a scoped-with on the deck to ensure we're the only thread using it right now.
        with deck:
            for k in range(deck.key_count()):
                # Draw the individual key images to each of the keys.
                if k != 0 and k != 1 and k != int(deck.key_count())-int(1):
                    deck.set_key_image(k, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"unselectedpfp\\pfp_{k}.jpg")).convert("RGBA")))
            deck.set_key_image(0, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\task_done.jpg")).convert("RGBA")))
            deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\help.jpg")).convert("RGBA")))
            deck.set_key_image(int(deck.key_count())-int(1), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"ICON\\close.jpg")).convert("RGBA")))
        
        # Register callback function for when a key state changes.
        deck.set_key_callback(key_press)

        # Wait until all application threads have terminated (for this example, this is when all deck handles are closed).
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                pass