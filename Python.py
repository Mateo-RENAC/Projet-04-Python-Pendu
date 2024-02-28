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
        print(self.listUnderscore)
        return self.listUnderscore

    def EstdansListLettreEntree(self,lettre):
        '''EstdansListLettreEntree renvoie un booléen si la lettre en paramètre est dans Listlettre'''
        for i in self.listeLettre :
            if self.listeLettre[i] == lettre :
                return True
        return False

    def ChoixMot(self):
        '''Demande a l'utilisateur le mot qui devra être trouvé'''

        self.mot = input("Choissisez un mot \n")
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
    
    


    
Pendu = Game()
Pendu.ChoixMot()
Pendu.Underscore(Pendu.GetMot())



