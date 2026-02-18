#Terminal-based TTT game
game =  ["-","-","-",
         "-","-","-",
         "-","-","-"]

gnabois = True

readyupplaya = "X"

def display_ze_game():
    print(game[0] + " | " + game[1] + " | " + game[2] + "      " + "1|2|3")
    print(game[3] + " | " + game[4] + " | " + game[5] + "      " + "4|5|6")
    print(game[6] + " | " + game[7] + " | " + game[8] + "      " + "7|8|9")

def playas():
    print("Pick your playa - X or O")
    p1 = input("Playa1: ")
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print("Playa2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Playa2: " + p2)
    elif p1 != "O" or p1 != "X":
        print("Specifics, mate. Specifics. Type X or O")
        play_ze_game()

def domain_of_ze_playa():
    global readyupplaya
    print("You are up, playa: " + readyupplaya)
    domain = input("Choose your domain: ")

    ForReal = False
    while not ForReal:
        while domain not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            domain = input("Choose your domain: ")
        domain = int(domain) - 1

        if game[domain] == "-":
            ForReal = True
        else:
            print("Domains cannot intersect with each other, set different coordinates.")
    game[domain] = readyupplaya
    display_ze_game()

def play_ze_game():
    print("Tic Tac Toe, Ready To Go!")
    display_ze_game()
    playas()

    while gnabois:
        domain_of_ze_playa()
        
        
        def who_ze_winna():
            global gnabois
            if game[0] == game[1] == game[2] != "-":
                gnabois = False
                print("Winna Winna " + game[0]+" it's chicken dinna!")
            elif game[3] == game[4] == game[5] != "-":
                gnabois = False
                print("Winna Winna " + game[3]+" it's chicken dinna!")
            elif game[6] == game[7] == game[8] != "-":
                gnabois = False
                print("Winna Winna " + game[6]+" it's chicken dinna!")
            elif game[0] == game[3] == game[6] != "-":
                gnabois = False
                print("Winna Winna " + game[0]+" it's chicken dinna!")
            elif game[1] == game[4] == game[7] != "-":
                gnabois = False
                print("Winna Winna " + game[1]+" it's chicken dinna!")
            elif game[2] == game[5] == game[8] != "-":
                gnabois = False
                print("Winna Winna " + game[2]+" it's chicken dinna!")
            elif game[0] == game[4] == game[8] != "-":
                gnabois = False
                print("Winna Winna " + game[0]+" it's chicken dinna!")
            elif game[2] == game[4] == game[6] != "-":
                gnabois = False
                print("Winna Winna "+ game[6]+" it's chicken dinna!")
            elif "-" not in game:
                gnabois = False
                print("Close fight, a winner would have been nice tho UWU")
                exit()
       
        def boogie_woogie():
            global readyupplaya
            if readyupplaya == "X":
                readyupplaya = "O"
            else:
                readyupplaya = "X"
        boogie_woogie()
        who_ze_winna()

play_ze_game()






