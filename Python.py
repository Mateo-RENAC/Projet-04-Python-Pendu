class Game :

    def __init__(self) :
        self.Pseudo = None
        self.Mot = None
        self.Listunderscore = None
        return

    def DemandePseudo(self):
        '''DemandePseudo()
        Demande à l'utilisateur
        un Pseudonyme et le met 
        dans la variable Pseudo'''
        self.Pseudo = input("Choissisez un Pseudonyme :\n")
        return
    
    def underscore(self, motacacher):
        '''underscore(motcacher)
        prend en paramètre une 
        chaine de caractère et 
        la transforme en une 
        liste de underscore de 
        même taille'''
        taillemot = len(motacacher)
        self.Listunderscore = []
        for i in range(taillemot):
            self.Listunderscore.append("_")
        self.Listunderscore = ''.join(self.Listunderscore)
        print(self.Listunderscore)
        return self.Listunderscore

    
    def ChoixMot(self):
        self.Mot = input("Choissisez un mot \n")
        return
    
    def getMot(self) :
        return self.Mot
    
    def getPseudo(self) :
        return self.Pseudo
    
    


    
Pendu = Game()
Pendu.ChoixMot()
Pendu.underscore(Pendu.getMot())



