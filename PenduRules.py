from DB import *

class Game :


    def __init__(self) :
        '''Initialise les variables principale du jeux'''

        self.pseudo = None
        self.mot = None
        self.listUnderscore = []
        self.listeLettre = []
        return


    def DemandePseudo(self):
        '''DemandePseudo()
        Demande à l'utilisateur
        un Pseudonyme et le met 
        dans la variable Pseudo'''

        self.pseudo = input("Choissisez un Pseudonyme :\n")
        return
    

    def Underscore(self, motacacher):
        '''underscore(motcacher)
        prend en paramètre une 
        chaine de caractère et 
        la transforme en une 
        liste de underscore de 
        même taille'''

        taillemot = len(motacacher)
        for i in range(taillemot):
            self.listUnderscore.append("_")
        self.listUnderscore = ''.join(self.listUnderscore)
        return self.listUnderscore


    def EstdansListLettreEntree(self,lettre):
        '''EstdansListLettreEntree renvoie un booléen si la lettre en paramètre est dans Listlettre'''
        for i in range(len(self.listeLettre)) :
            if self.listeLettre[i] == lettre :
                return True
        return False

    def AjouteLettre(self, lettre) :
        '''AjouteLettre ajoute la lettre choisie dans ListeLettreEntree'''
        self.listeLettre.append(lettre)
        return

    def EstDansLeMot(self, lettre, mot):
        '''Fonction qui détecte si la lettre choisie est dans le mot choisi,
        si c'est le cas elle remplace dans underscore la lettre à l'index de celle-ci et renvoie True
        Sinon elle renvoie False'''

        found = False  # Variable pour indiquer si la lettre a été trouvée dans le mot
        for i in range(len(mot)):
            if mot[i] == lettre:  # Condition si la lettre est dans le mot
                self.listUnderscore = self.listUnderscore[:i] + lettre + self.listUnderscore[i + 1:]
                found = True  # Indique que la lettre a été trouvée
        if found:
            self.AjouteLettre(lettre)  # Ajoute la lettre à la liste des lettres entrées
        else:
            self.AjouteLettre(lettre)  # Ajoute la lettre même si elle n'est pas trouvée dans le mot
        return found


    def ChoixMot(self):
        '''Demande a l'utilisateur le mot qui devra être trouvé'''

        self.mot = input("Choissisez un mot \n")
        self.mot = str(self.mot)
        return


    def GetListeLettreEntree(self) :
        '''retourne la liste des lettre déjà entrée'''

        return self.listeLettre


    def GetMot(self) :
        '''retourne le mot qui doit être trouvé'''

        return self.mot


    def GetPseudo(self) :
        '''retourne le pseudonyme de l'utilisateur'''

        return self.pseudo
    
    def GetUnderscore(self) :
        '''retourne la chaine de caractère underscore'''
        return self.listUnderscore

def MotRandom(self) :
    '''Demande à l'utilisateur un niveau de difficulté
    et utilise la fonction ObtenirMotAleatoire de DB.py 
    déposé ensuite dans self.mot'''
    Reponse = input("Qu'elle difficulté ?\n")
    self.mot = ObtenirMotAleatoire(Reponse)
    return