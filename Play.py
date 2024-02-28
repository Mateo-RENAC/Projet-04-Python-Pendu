from PenduRules import *

def Play() :
    '''Fonction permettant de faire fonctionner le jeux du Pendu'''
    Pendu = Game()
    Pendu.DemandePseudo()
    Pendu.ChoixMot()
    Pendu.Underscore(Pendu.mot)
    essais = 0
    while essais < 5 and Pendu.GetMot() != Pendu.GetUnderscore() :
        print(Pendu.GetUnderscore())
        if len(Pendu.GetListeLettreEntree()) < 0 :
            print(Pendu.GetListeLettreEntree())
        print("Nombre d'essais : " ,essais)
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