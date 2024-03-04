from PenduRules import *
from Affichage import *
from DB import *
import os


def Play() :
    '''Fonction permettant de faire fonctionner le jeux du Pendu'''
    Pendu = Game()
    Pendu.DemandePseudo()
    Pendu.MotRandom()
    Pendu.Underscore(Pendu.mot)
    essais = 0

    while essais < 8 and Pendu.GetMot() != Pendu.GetUnderscore() :
        clear_console()
        print(Pendu.mot)
        echaffaud(essais)                                                       #Affiche l'échaffaud
        print(Pendu.GetUnderscore())                                            #Affiche le mot transformé en underscore
        if len(Pendu.GetListeLettreEntree()) < 0 :
            print(Pendu.GetListeLettreEntree())                                 #Affiche la liste des lettres entrées si celle-ci a au moins 1 lettre
        print("Nombre d'essais : " ,essais)                                     #Affiche le nombre d'essais
        lettreessayer = input("entrez une lettre \n")
        #lettreessayer contient l'entrée du joueur                           
        lettreessayer = str(lettreessayer)

        if lettreessayer == 'restart' :
            return Play()
        if lettreessayer == 'exit' :
            return 'EXIT_SUCCESS'
        
        if lettreessayer == 'scores' :
            return ScoreFonct()

        elif Pendu.EstdansListLettreEntree(lettreessayer) :
            print("Déjà rentrée essayez une autre lettre")

        elif Pendu.EstDansLeMot(lettreessayer,Pendu.mot) == False :
            essais += 1

    if Pendu.GetMot() == Pendu.GetUnderscore() :
        print("Victoire ! le mot était bien : " + Pendu.mot)
        SauvegarderScore(Pendu.GetPseudo(), 'oui', Pendu.Difficulty)
        return
    
    else:
        print("Pendu ! le mot était : " + Pendu.mot)
        SauvegarderScore(Pendu.GetPseudo(), 'non', Pendu.Difficulty)
        return


def ScoreFonct() :
    '''Un affichage pour les Scores'''
    clear_console()
    commandesScore()
    entree = input()
    while entree != 'exit' :
        if entree == 'Alpha' :
            AfficherScoresAlphabetique()
            entree = input()
        elif entree == 'Score' :
            AfficherScoresBase()
            entree = input()
        elif entree == 'ScoreDec' :
            AfficherScoresParScoreDecroissant()
            entree = input()
        elif entree == 'Difficulté' :
            AfficherScoresParDifficulte()
            entree = input()
        else :
            print("Commande Non reconnue")
            return ScoreFonct
    clear_console()
    return Play()
    


Play()