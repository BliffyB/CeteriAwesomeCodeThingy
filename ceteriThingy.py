import random
import os,time
# Main menu
def main_menu():
    print ("1. Ceteri's collage resheach papers about (Are traps gay?)")
    print ("2. That ass ;D")
    print ("\n0. Quit")
    choice = input(" >>  ")


    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return
# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()

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

    
# =======================
#    MENUS DEFINITIONS
# =======================
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': trapsAre,
    '2': datAss,
    '9': back,
    '0': exit,
}



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

main_menu()
# print ("oh wait we have no data here. Thanks bliffy you lazy poop")


print ("1. Menu 1")
print ("2. Menu 2")
print ("3. That ass ;D")
print ("4. Ceteri's collage resheach papers about (Are traps gay?)")
print ("\n0. Quit")
choice = input(" >>  ")
print ("oh wait we have no data here. Thanks bliffy you lazy poop")


