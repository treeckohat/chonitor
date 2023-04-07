#Leon
from cryptography.fernet import Fernet

with open('moraBankUserInfo.key', 'rb') as filekey:
  key = filekey.read()    
fernet = Fernet(key) #calls the key

def writeTotxtFile(userList): #writes data to txt file, encrypted
  global fernet
  userInfoList = [] #list for all entries into database
  for user, values in userList.items():
    newList = []
    newList.append(user)
    for i in values:
      newList.append(i)
    newString = '/'.join(newList) #creates a string in data/data/data/data/data format
    userInfoList.append(newString)
  encryptionString = '\n'.join(userInfoList) #the text being encrypted
  encrypted = fernet.encrypt(bytes(encryptionString, "utf8")) #encrypts string
  with open('moraBankUserInfo.txt', 'wb') as encryptedFile: #writes the encryted text
    encryptedFile.write(encrypted)
  
def createUserList():
  global fernet
  userDict = {} #makes the dictionary
  with open('moraBankUserInfo.txt', 'rb') as encryptedFile:
    encrypted = encryptedFile.read()
  decrypted = fernet.decrypt(encrypted).decode("utf8") #decodes
  users = decrypted.split('\n') #splits into individual users
  for userDetails in users:
    userDetails = userDetails.rstrip() #rids unecessary whitespace
    splitUserDetails = userDetails.split('/')
    userDict[splitUserDetails[0]] = splitUserDetails[1:] #turns it into required dictionary format
    # {data: [data,data,data,data]}
  return userDict