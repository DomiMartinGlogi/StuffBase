import sys
import time
import json
import os

Stuff = {}

# TODO
# Menu

SleepTime = 0.1

def Menu():
    print("1 : Save the current State")
    time.sleep(SleepTime)
    print("2 : Store something")
    time.sleep(SleepTime)
    print("3 : Modify Something")
    time.sleep(SleepTime)
    print("4 : Look for Something")
    time.sleep(SleepTime)
    print("5 : Delete Something")
    time.sleep(SleepTime)
    print("Functions 6 - 8 are currently unused")
    time.sleep(SleepTime)
    print("9 : End the Session")
    time.sleep(SleepTime)
    RawInput = input("Your Answer: ")
    Ans = int(RawInput)

    # Selection of What to do
    if Ans == 1:
        Save()
    elif Ans == 2:
        StoreSomething()
    elif Ans == 3:
        ModifySomething()
    elif Ans == 4:
        Search()
    elif Ans == 5:
        RemoveSomething()
    elif Ans == 9:
        print("Session ended")
        sys.exit()
    else:
        print("No valid input!")
        Menu()


def Save():
    Data = Stuff
    file = open("Stuffbase.json", "w")
    json.dump(Data, file, indent = 1)
    file.flush()
    file.close()
    Menu()

def Search():
    SearchKey = input("Search for: ")
    Result = dict(filter(lambda item: SearchKey in item[0], Stuff.items()))
    print("Results: " + str(Result))
    input("Press enter to continue!")
    Menu()


def StoreSomething():
    Object = input("Object: ")
    Place = input("Place: ")
    Storage = input("Storage: ")
    Status = input("Status: ")
    n = 0
    while Object in Stuff:
        n = n + 1
        Object = Object + str(n)
    Stuff[Object] = {"Place": Place, "Storage": Storage, "Status": Status}
    Menu()

def ModifySomething():
    Object = input("Object: ")
    print(Stuff[Object])
    ObjectSubDict = Stuff[Object]                   #ObjectSubDict used for modification of the Objects parameters.
    Place = input("Place: ")
    Storage = input("Storage: ")
    Status = input("Status: ")
    if Place != "":
        ObjectSubDict["Place"] = Place
    if Storage != "":
        ObjectSubDict["Storage"] = Storage
    if Status != "":
        ObjectSubDict["Status"] = Status
    Stuff[Object] = ObjectSubDict
    Menu()


def RemoveSomething():
    Object = input("Object: ")
    print(Stuff[Object])
    if not Object in Stuff:
        print("Object not in the Database!")
    else:
        Stuff.pop(Object)
        print(Object + " was deleted!")
    Menu()

#Initial loading of file:

with open("Stuffbase.json") as StuffBase:
    Stuff = json.load(StuffBase)
Menu()
