from cryptography.fernet import Fernet

with open('moraBankUserInfo.key', 'rb') as filekey:
  key = filekey.read()    
fernet = Fernet(key) #calls the key


choice = input("e or d or b ")
if choice == "d":
    with open('moraBankUserInfoENCRYPTED.txt', 'rb') as encryptedFile:
        encrypted = encryptedFile.read()
    decrypted_message = fernet.decrypt(encrypted)
    print(decrypted_message)

if choice == "e":
    msg = """monkey/1234/15272/30/5
monkman/5656/777/20/100
luffy/8008/50/0/50
dunne/1111/1000/0/0
kaibinky/5189/100000/20/40
amongus187/3967/69/40/85
mank0/5678/24356/230/170
mongol/3000/3000/30/30
jeans/7777/7777/70/45
poor/0000/0/0/1000"""
    encrypted_message = fernet.encrypt(bytes(msg, "utf8"))
    with open('moraBankUserInfoENCRYPTED.txt', 'wb') as encryptedFile: #writes the encryted text
        encryptedFile.write(encrypted_message)

if choice == 'b':
    with open('moraBankUserInfoENCRYPTED.txt', 'wb') as en: #writes the encryted text
        for key, value in msg.items(): 
            en.write(fernet.encrypt(bytes('%s:%s\n' % (key, value), "utf8")))

input("bruh ")

