import threading
## Defining a method  
def sctn():  
    run = False
    print("end the code")  
S = threading.Timer(5.0, sctn) 
S.start()  
print("Exit Program\n")

import threading
## Defining a method  
def sctn():  
   print("SECTION FOR LIFE \n")  
S = threading.Timer(5.0, sctn) 
S.start()  
print("Exit Program\n")

'''
import time
from threading import Thread
import msvcrt

def task1():
    while True:
        print("cum")
        time.sleep(5)

def task2():
    while True:
        if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:
            answer = input("Are you sure? Y/N ")
            while answer != 'Y':
                answer = input("Are you sure? Y/N ")
            if answer == 'Y':
                print('escape')
            if answer == 'N':
                print('returned')

start_time = time.perf_counter()

# create two new threadsa
t1 = Thread(target=task1)
t2 = Thread(target=task2)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = time.perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
'''