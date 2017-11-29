#Little comment

#Comment: build your own defintions
def greeting():
    print("Hello")

    answer = input("What is your name?")
    print("It's nice to meet you " + answer)


def living_room():
    print("you are in the living room")
    choice = int(input("1 to enter kitchen\n2 to enter hallway\n3 to open front door"))
    if choice == 1:
        kitchen()
    elif choice == 2:
        hallway()
    elif choice == 3:
        front_door()
    else:
        print("try again")
        living_room()

def front_door():
    print("the door is locked from the outside")
    choice = int(input("1 to try open door using force"))
    if wardrobe_count >= 2:
        choice = int(input("1 to try open the door using force\n2 to use the spoo-key"))
    if choice == 1:
        print("you could not open the door because it is locked")
        living_room()
    elif choice == 2:
        print("congrats")
        success()
    else:
        print("try again")
        front_door()


def kitchen():
    print("you are in the kitchen")
    choice = int(input("1 to enter living room\n2 to enter bathroom\n3 to look at calender"))
    if choice == 1:
        living_room()
    elif choice == 2:
        bathroom()
    elif choice == 3:
        print("you look at the calender...it is november 17th")
        kitchen()
    else:
        print("try again")
        kitchen()

def bathroom():
    print("you are in the bathroom")
    choice = int(input("1 to enter hallway\n2 to enter kitchen\n3 to look in mirror"))
    if choice == 1:
        hallway()
    elif choice == 2:
        kitchen()
    elif choice == 3:
        mirror()
    else :
        print("try again")
        bathroom()

def mirror():
    global mirror_count
    mirror_count = mirror_count + 1
    if mirror_count == 1:
        print("it's you")
    elif mirror_count == 2:
        print("you see your reflection")
    elif mirror_count == 3:
        print("it's still you")
    elif mirror_count == 4:
        print("you carefully try watch yourself blink but it doesn't work because that's impossible")
    elif mirror_count == 5:
        print("you think about how looking at yourself for this long is really freaking you out...you should probably stop")
    elif mirror_count == 6:
        print("this is your fault not mine")
        death_death()
    choice = int(input("1 to keep looking in mirror\n2 to stop looking in mirror"))
    if choice == 1:
        mirror()
    elif choice == 2:
        print("you stopped looking in the mirror")
        bathroom()
    else:
        print("try again")
        mirror()

def bedroom():
    print("you are in the bedroom")
    choice = int(input("1 to enter hallway\n2 to enter bathroom\n3 to look at window"))
    if choice == 1:
        hallway()
    elif choice == 2:
        bathroom()
    elif choice == 3:
        window()
    else:
        print("try again")
        bedroom()

def hallway():
    print("you are in the hallway")
    choice = int(input("1 to enter living room\n2 to enter bathroom\n3 to go up the stairs to the attic"))
    if choice == 1:
        living_room()
    elif choice == 2:
        bathroom()
    elif choice == 3:
        attic()
    else:
        print("try again")
        hallway()

def window():
    print("you look at the window")
    choice = int(input("1 to keep looking at window\n2 to stop looking at window"))
    if choice == 1:
        print("it is a window")
        window()
    elif choice == 2:
        print("you stopped looking at the window")
        bedroom()
    elif choice == 3:
        print("eyes are the window to the soul but this is just a window")
        death_death()
    else:
        print("try again")
        bedroom()

def attic():
    print("you are in the attic")
    choice = int(input("1 to go back downstairs\n2 to look at wardrobe"))
    if choice == 1:
        print("you went back downstairs")
        hallway()
    elif choice == 2:
        print("you look at the wardrobe")
        wardrobe()
    else:
        print("try again")
        attic()

def wardrobe():
    global wardrobe_count
    wardrobe_count = wardrobe_count + 1
    print("it looks like a wardrobe")
    if wardrobe_count == 1:
        print("something glimmers in the back right corner")
        attic()
    elif wardrobe_count == 2:
        print("congrats! you found the spoo-key")
        attic()
    elif wardrobe_count == 3:
        print("you found narnia")
        attic()
    elif wardrobe_count == 4:
        print("narnia is cold...you should have brought a jacket")
        death_death()

    choice = int(input("1 to look inside wardrobe\n2 to stop looking at wardrobe"))
    if choice == 1:
        wardrobe()
    elif choice == 2:
        print("you stopped looking at the wardrobe")
        attic()
    else:
        print("try again")
        wardrobe()



def death_death():
    print("@@@ @@@   @@@@@@   @@@  @@@     @@@@@@@   @@@  @@@@@@@@  @@@@@@@")
    print("@@@ @@@  @@@@@@@@  @@@  @@@     @@@@@@@@  @@@  @@@@@@@@  @@@@@@@@")
    print("@@! !@@  @@!  @@@  @@!  @@@     @@!  @@@  @@!  @@!       @@!  @@@")
    print("!@! @!!  !@!  @!@  !@!  @!@     !@!  @!@  !@!  !@!       !@!  @!@")
    print("!@!@!   @!@  !@!  @!@  !@!     @!@  !@!  !!@  @!!!:!    @!@  !@!")
    print("@!!!   !@!  !!!  !@!  !!!     !@!  !!!  !!!  !!!!!:    !@!  !!!")
    print("!!:    !!:  !!!  !!:  !!!     !!:  !!!  !!:  !!:       !!:  !!!")
    print(":!:    :!:  !:!  :!:  !:!     :!:  !:!  :!:  :!:       :!:  !:!")
    print("::    ::::: ::  ::::: ::      :::: ::   ::   :: ::::   :::: ::")
    print(":      : :  :    : :  :      :: :  :   :    : :: ::   :: :  :")

    sys.exit(0)

def success():
    print("  __   __   U  ___ u   _   _       ____              ____                     _____   ")
    print("  \ \ / /   \/''_ \ /U |''|u| |   |  _''\    ___   |  _''\          ___     |_ ''_|  ")
    print("   \ V /     | | | | \| |\| |    /| | | |  |_''_| /| | | |        |_''_|      | |    ")
    print(" U_|''|_u.-,_| |_| |  | |_| |    U| |_| |\  | |   U| |_| |\         | |      /| |\   ")
    print("    |_|   \\_)-\\___/  <<\\___/      |____/ uU/| |\\u  |____/ u       U/| |\\u   u |_|U   ")
    print(".-,//|(_       \\   (__) )(        |||_.-,_|___|_,-.|||_       .-,_|___|_,-._// \\_  ")
    print(" \_) (__)     (__)      (__)      (__)_)\_)-' '-(_/(__)_)       \_)-' '-(_/(__) (__) ")

    sys.exit(0)

#Start Code Here:
mirror_count = 0
wardrobe_count = 0
print("  .-')     _ (`-.                           .-. .-')                       .-')      ('-.   ('-.     _  .-')             ('-. .-.")
print(" ( OO ).  ( (OO  )                          \  ( OO )                     ( OO ).  _(  OO) ( OO ).-.( \( -O )           ( OO )  //")
print("_)---\_)_.`     \ .-'),-----.  .-'),-----. ,--. ,--.   ,--.   ,--.      (_)---\_)(,------./ . --. / ,------.   .-----. ,--. ,--.")
print("\  :` `. |  /  | |/   |  | |  |/   |  | |  ||      /,  .-')     /        \  :` `.  |  |  .-'-'  |  | |  /  | | |  |('-. |   .|  |")
print(" '..`''.)|  |_.' |\_) |  |\|  |\_) |  |\|  ||     ' _)(OO  \   /          '..`''.)(|  '--.\| |_.'  | |  |_.' |/_) |OO  )|       |")
print("\       /|  |        `'  '-'  '   `'  '-'  '|  |\   \  `-./  /.__)       \       / |  `---.|  | |  | |  |\  \(_'  '--'\ |  | |  |")
print(" `-----' `--'          `-----'      `-----' `--' '--'    `--'             `-----'  `------'`--' `--' `--' '--'  `-----' `--' `--' ")
print("you wake up suddenly and look around the room")
bedroom()
