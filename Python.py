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

    def EstDansLeMot(self, lettre, mot) :
        '''Fonction qui détecte si la lettre choisie est dans le mot choisie,
        si c'est le cas elle remplace dans underscore la lettre a l'indexe de celle-ci et renvoie True
        Sinon il renvoie False'''
        for i in range(len(mot)) :
            occurence = 0
            if mot[i] == lettre :                       #Condition si la lettre est dans le mot
                underscoretemp = []
                for caractere in self.listUnderscore :  #Je créer une variable temporaire sous forme de liste pour pouvoir changer la chaine de caractère + facilement
                    underscoretemp.append(caractere)
                underscoretemp[i] = lettre
                underscoretemp = ''.join(underscoretemp)    #Je transforme la liste temporaire en chaine de caractère
                self.listUnderscore = underscoretemp
                if occurence < 1 :
                    self.AjouteLettre(lettre)
                    occurence += 1    
                return True
        self.AjouteLettre(lettre)
        return False


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


