import sqlite3

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

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute("INSERT INTO record VALUES (:uid, :name, :email, :contact, :password, :last_time1, :average_time1, :total_time1, :last_time2, :average_time2, :total_time2, :last_time3, :average_time3, :total_time3)", {
                'uid': '0',
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

uid = 0
for row in con.execute("Select * from record"):
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print(row[6])
    print(row[7])
    print(row[8])
    print(row[9])
    print(row[10])
    print(row[11])
    print(row[12])
    print(row[13])
    uid = uid + 1


sql = ''' UPDATE record
            SET uid = ? ,
                email = ? ,
                contact = ?
            WHERE uid = ?'''
cur = con.cursor()
cur.execute(sql,(str(uid),"e@gmail.com", 423, '0'))
con.commit()



    '''
    try:
        deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        deck.set_key_image(2, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        deck.set_key_image(3, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        last = True
    except:
        pass
    try:
        deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"pfp_{(3 * page) - 1}.jpg")).convert("RGBA")))
        deck.set_key_image(2, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        deck.set_key_image(3, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        last = True
    except:
        pass
    try:
        deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"pfp_{(3 * page) - 1}.jpg")).convert("RGBA")))
        deck.set_key_image(2, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"pfp_{(3 * page)}.jpg")).convert("RGBA")))
        deck.set_key_image(3, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"end.jpg")).convert("RGBA")))
        last = True
    except:
        pass
    try:
        deck.set_key_image(1, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"pfp_{(3 * page) - 1}.jpg")).convert("RGBA")))
        deck.set_key_image(2, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"pfp_{(3 * page)}.jpg")).convert("RGBA")))
        deck.set_key_image(3, image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"pfp_{(3 * page) + 1}.jpg")).convert("RGBA")))
        deck.set_key_image(int(deck.key_count())-int(2), image_format(deck,Image.open(os.path.join(ASSETS_PATH, f"next.jpg")).convert("RGBA")))
        last = False
    except:
        pass
    '''

        image0 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_0.jpg")).convert("RGBA"))
        image1 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_1.jpg")).convert("RGBA"))
        image2 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_2.jpg")).convert("RGBA"))
        image3 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_3.jpg")).convert("RGBA"))
        image4 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_4.jpg")).convert("RGBA"))
        image5 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_5.jpg")).convert("RGBA"))
        image6 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_6.jpg")).convert("RGBA"))
        image7 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_7.jpg")).convert("RGBA"))
        image8 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_8.jpg")).convert("RGBA"))
        image9 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_9.jpg")).convert("RGBA"))
        image10 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_10.jpg")).convert("RGBA"))
        image11 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_11.jpg")).convert("RGBA"))
        image12 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_12.jpg")).convert("RGBA"))
        image13 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_13.jpg")).convert("RGBA"))
        image14 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_14.jpg")).convert("RGBA"))
        image15 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_15.jpg")).convert("RGBA"))
        image16 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_16.jpg")).convert("RGBA"))
        image17 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_17.jpg")).convert("RGBA"))
        image18 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_18.jpg")).convert("RGBA"))
        image19 = image_format(deck,Image.open(os.path.join(ASSETS_PATH, "pfp_19.jpg")).convert("RGBA"))
