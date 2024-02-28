class Game :

    def __init__(self) :
        '''Initialise les variables principale du jeux'''
        self.Pseudo = None
        self.Mot = None
        self.Listunderscore = []
        self.Listelettre = []
        return

    def DemandePseudo(self):
        '''DemandePseudo()
        Demande à l'utilisateur
        un Pseudonyme et le met 
        dans la variable Pseudo'''

        self.Pseudo = input("Choissisez un Pseudonyme :\n")
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
            self.Listunderscore.append("_")
        self.Listunderscore = ''.join(self.Listunderscore)
        print(self.Listunderscore)
        return self.Listunderscore


    def ChoixMot(self):
        '''Demande a l'utilisateur le mot qui devra être trouvé'''
        self.Mot = input("Choissisez un mot \n")
        return


    def GetListeLettreEntree(self) :
        '''retourne la liste des lettre déjà entrée'''
        return self.Listelettre


    def GetMot(self) :
        '''retourne le mot qui doit être trouvé'''
        return self.Mot


    def GetPseudo(self) :
        '''retourne le pseudonyme de l'utilisateur'''
        return self.Pseudo
    
    


    
Pendu = Game()
Pendu.ChoixMot()
Pendu.Underscore(Pendu.GetMot())



