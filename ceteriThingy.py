import random
import os,time

def menu(choice):
    if (choice == 0): print('Saturday0')
    if (choice == 1): print('Saturday0')           
    if (choice == 2): print('Saturday0')         
    if (choice == 3): datAss
    if (choice == 4): tarpsAre

def trapsAre():
    print ("whalcume to are grat skdjaklajawkljafaf")
    print (" -incerts all the stuff about traps ")
    print (" might just make txt file and have it import here ")

def datAss():
    frames.append (f.readlines())


os.system('cls')
filenames = ["new1"]
frames = []
for name in filenames:
    with open(name,"r",encoding="utf8") as f:
        frames.append (f.readlines())

for frame in frames:
    print("".join(frame))
    time.sleep(1)
print("\n")
name = input('Hello there what is your name?\n')
if (name.lower() == "mark"): name = random.choice( ['yarini', 'yarpini', 'i cant say your user name it too hard :( '] )   
if (name.lower() == "boomzy"): raise Exception('Nice try ape') 
print("hi "+ name) 
guildname = random.choice( ['A dead guild', 'ceteri', 'shiteri'] )
print("whalecome to the super awesome "+ guildname + " database \n ")
print ("What you like to acess? :")
print ("1. Menu 1")
print ("2. Menu 2")
print ("3. That ass ;D")
print ("4. Ceteri's collage resheach papers about (Are traps gay?)")
print ("\n0. Quit")
choice = input(" >>  ")
print ("oh wait we have no data here. Thanks bliffy you lazy poop")

