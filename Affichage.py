import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def echaffaud(Etat) :
    if Etat == 0:
        print(" ==========Y= ")
    if Etat <= 1 :
        print(" ||/       |  ")
    if Etat <= 2 :
        print(" ||/       |  ")
    if Etat <= 3 :
        print(" ||        0  ")
    if Etat <= 4 :
        print(" ||       /|\ ")
    if Etat <= 5 :
        print(" ||        |")
    if Etat <= 6 :
        print(" ||       / \ ")
    if Etat <= 7 :                    
        print("/||           ")
    if Etat <= 8 :
        print("==============\n")