import os


def clear_console():
    '''Efface tout ce qui a été écrit précedement dans la console'''
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def echaffaud(Etat) :
    '''
    En Fonction du nombre d'essais,
    l'échafaud se construit
    '''
    if Etat == 8:
        print(" ==========Y= ")
    if Etat >= 7 :
        print(" ||/       |  ")
    if Etat >= 6 :
        print(" ||/       |  ")
    if Etat >= 5 :
        print(" ||        0  ")
    if Etat >= 4 :
        print(" ||       /|\ ")
    if Etat >= 3 :
        print(" ||        |")
    if Etat >= 2 :
        print(" ||       / \ ")
    if Etat >= 1 :                    
        print("/||           ")
    if Etat >= 0 :
        print("==============\n")

def commandesPlay() :
    print("Commandes : \n"
          "-exit : vous renvoie à l'écran titre sans sauvegarder\n"
          "-restart : recommence le jeux, le jeux en cours ne sera pas sauvegardé\n")

def commandesScore() :
    print("Commandes : \n"
          "-Alpha : Ordonne par ordre alphabétique\n"
          "-Score : Ordonne par ordre de score croissant\n"
          "-ScoreDec : Ordonne par ordre de score décroissant\n"
          "-Difficulté : Ordonne les parties par difficulté\n"
          "-exit : Sort de l'affichage des scores et allume le jeux\n")

def AffichageIntro():
    '''Ecran Titre et affichage de plusieurs commandes comme -Jouer ou -Scores'''
    print(".----------------.  .----------------.  .-----------------. .----------------.  .----------------.\n")
    print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |\n")
    print("| |   ______     | || |  _________   | || | ____  _____  | || |  ________    | || | _____  _____ | |\n")
    print("| |  |_   __ \   | || | |_   ___  |  | || ||_   \|_   _| | || | |_   ___ `.  | || ||_   _||_   _|| |\n")
    print("| |    | |__) |  | || |   | |_  \_|  | || |  |   \ | |   | || |   | |   `. \ | || |  | |    | |  | |\n")
    print("| |    |  ___/   | || |   |  _|  _   | || |  | |\ \| |   | || |   | |    | | | || |  | '    ' |  | |\n")
    print("| |   _| |_      | || |  _| |___/ |  | || | _| |_\   |_  | || |  _| |___.' / | || |   \ `--' /   | |\n")
    print("| |  |_____|     | || | |_________|  | || ||_____|\____| | || | |________.'  | || |    `.__.'    | |\n")
    print("| |              | || |              | || |              | || |              | || |              | |\n")
    print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |\n")
    print("'----------------'  '----------------'  '----------------'  '----------------'  '----------------'\n")
    print(""" 
    Commandes :
    -Jouer : Commence le jeux du Pendu\n
    -Score : Affiche les scores\n
    -Exit : ferme le programme\n      
          """)