import pikepdf
import queue
import threading
import time
import sys

wordqueue = queue.Queue()

def getInfo():

    global target_file
    global wordlist
    global numthreads

    while True:

        print("Enter Wordlist:")

        try:
            wordlist = str(input(">>> "))
            if ".txt" not in wordlist:
                wordlist = wordlist + ".txt"

            break

        except:
            print("INVALID INPUT")


    while True:

        print("Enter Target Pdf:")

        try:
            target_file = str(input(">>> "))
            if ".pdf" not in target_file:
                target_file = target_file + ".pdf"

            break

        except:
            print("INVALID INPUT")


    while True:

        print("Number of Threads:")

        try:
            numthreads = int(input(">>> "))
            if numthreads < 1:
                print("INVALID INPUT")
                continue

            else:
                break

        except:
            print("INVALID INPUT")






def makeWordqueue():
    try:
        file1 = open(wordlist , "r")
        for line in file1:
            wordqueue.put(line.strip())

        file1.close()

    except FileNotFoundError:
        print(f"NO FILE IN DIRECTORY CALLED {wordlist}")
        wordqueue.queue.clear()

    except:
        print(f"ERROR OPENING {wordlist}")
        wordqueue.queue.clear()

        


def attack():




    while not wordqueue.empty():

        password = wordqueue.get()



        try:
        
        
            pikepdf.Pdf.open(target_file , password = password)
            print("")
            print(f"PASSWORD :{password}")
            print("")
            wordqueue.queue.clear()

        except FileNotFoundError:
            print(f"NO FILE IN DIRECTORY CALLED {target_file}")
            wordqueue.queue.clear()

        except:
            continue




print("PDF CRACKER")
print("")

while True:

    getInfo()



    makeWordqueue()

    for i in range(numthreads):
        t = threading.Thread(target = attack , args = (),)
        t.start()


    while True:
        if wordqueue.empty():
            time.sleep(3)

            break
        else:
            continue


    print("Enter any key to continue , Q to quit")
    furtherattacks = str(input(">>> "))
    if furtherattacks.upper() == "Q":
        sys.exit()
    else:
        continue

    

    

    

    
