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
        underscore = []
        for i in taillemot :
            underscore[i].append("_")
        return underscore
    
    def ChoixMot(self):
        Mot = input("Choissisez un mot ")
        return Mot
    
Pendu = Game()
Pendu.ChoixMot()
Pendu.underscore()



