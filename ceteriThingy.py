import random
import os,time

"""main"""
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
name.lower() = input('Hello there what is your name?\n')
if (name == "mark"): name = random.choice( ['yarini', 'yarpini', 'i cant say your user name it too hard :( '] )   
if (name == "boomzy"): raise Exception('Nice try ape') 
print("hi "+ name) 
guildname = random.choice( ['A dead guild', 'ceteri', 'shiteri'] )
print("whalecome to the super awesome "+ guildname + " database \n ")
print ("What you like to acess? :")
print ("1. Menu 1")
print ("2. Menu 2")
print ("3. Menu 3")
print ("\n0. Quit")
choice = input(" >>  ")
print ("oh wait we have no data here. Thanks bliffy you lazy poop")
