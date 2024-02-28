class Game :

    Pseudo = None
    Mot = None

    def __init__(self) :
        return

    def DemandePseudo(self):
        '''DemandePseudo()
        Demande à l'utilisateur
        un Pseudonyme et le met 
        dans la variable Pseudo'''
        Pseudo = input("Choissisez un Pseudonyme :")
        return
    
    def underscore(self,motacacher) :
        '''underscore(motcacher)
        prend en paramètre une 
        chaine de caractère et 
        la transforme en une 
        liste de underscore de 
        même taille'''
        taillemot = len(motacacher)
        self.Listunderscore = []
        for i in range(taillemot-1) :
            self.Listunderscore[i].append("_")
        str(self.Listunderscore)
        return self.Listunderscore
    
    def ChoixMot(self):
        Mot = input("Choissisez un mot ")
        return Mot
    
Pendu = Game()
Pendu.ChoixMot()
Pendu.underscore()



