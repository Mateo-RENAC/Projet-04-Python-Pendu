from PenduRules import *
from Affichage import *
import os


def Play() :
    '''Fonction permettant de faire fonctionner le jeux du Pendu'''
    Pendu = Game()
    Pendu.DemandePseudo()
    Pendu.ChoixMot()
    Pendu.Underscore(Pendu.mot)
    essais = 0

    while essais < 5 and Pendu.GetMot() != Pendu.GetUnderscore() :
        clear_console()
        print(Pendu.GetUnderscore())                                            #Affiche le mot transformé en underscore
        if len(Pendu.GetListeLettreEntree()) < 0 :
            print(Pendu.GetListeLettreEntree())                                 #Affiche la liste des lettres entrées si celle-ci a au moins 1 lettre
        print("Nombre d'essais : " ,essais)                                     #Affiche le nombre d'essais
        lettreessayer = input("entrez une lettre \n")                           

        lettreessayer = str(lettreessayer)

        if Pendu.EstdansListLettreEntree(lettreessayer) :
            print("Déjà rentrée essayez une autre lettre")

        elif Pendu.EstDansLeMot(lettreessayer,Pendu.mot) == False :
            essais += 1

    if Pendu.GetMot() == Pendu.GetUnderscore() :
        print("Victoire ! le mot était bien : " + Pendu.mot)
        return
    
    else :
        print("Pendu ! le mot était : " + Pendu.mot)
        return

Play()