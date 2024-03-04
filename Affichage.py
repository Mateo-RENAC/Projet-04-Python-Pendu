import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def echaffaud(Etat) :
    '''
    En Fonction du nombre d'essais,
    l'échafaud se construit
    '''
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

def commandesPlay() :
    print("Commandes : \n"
          "-exit : vous sort du jeux sans sauvegarder\n"
          "-restart : recommence le jeux, le jeux en cours ne sera pas sauvegardé\n"
          "-scores : affiche le tableau des scores")

def commandesScore() :
    print("Commandes : \n"
          "-Alpha : Ordonne par ordre alphabétique"
          "-Score : Ordonne par ordre de score croissant"
          "-ScoreDec : Ordonne par ordre de score décroissant"
          "-Diffculté : Ordonne les parties par difficulté")

