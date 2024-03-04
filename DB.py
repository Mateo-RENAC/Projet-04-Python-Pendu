#Ici je vais gérer les requêtes avec Djangos

from PenduDjango.PenduDjangoapp.models import ModelScore
from django.db.models import Count, Case, When, CharField, Value, IntegerField


def AjouterScore(nomdujoueur, resultat) :
    '''Fonction qui envoie le score dans la base de donnée
    prend en paramètre le nom du joueur et la victoire ou 
    la défaite sous forme de 'oui' ou 'non'
    ''' 
    if resultat != 'oui' and resultat != 'non' :
        print("Le résultat doit être oui ou non")
        return 
    nouveauresultat = ModelScore()
    nouveauresultat.save()
    print("Score sauvegardé ! avec le pseudo : " + str(nomdujoueur))
    return 


def AfficherScore10Derniers() :
    '''
    Affiche les 10 derniers scores enregistré dans la base de donnée
    '''
    entrees = ModelScore.objects.order_by('-id')[:10]
    print("Scores : \n")
    for entree in entrees:
        print(f"Nom: {entree.nom}, Victoire: {entree.win}")
    return


def AfficherScoreOrdreAlphabétique() :
    '''
    Affiche les scores enregistré dans l'ordre alphabétique
    '''
    entrees = ModelScore.objects.order_by('-nom')
    print("Scores : \n")
    for entree in entrees :
        print(f"Nom: {entree.nom}, Victoire: {entree.win}")
    return

def AfficherScore() :
    '''
    Affiche les Scores (nombre de Victoire)    
    '''
    # Récupérer les données groupées et compter le nombre de "oui"
    scores = ModelScore.objects.annotate(victoire=Count(Case(When(win="oui", then=1), output_field=IntegerField()))).values('id', 'nom', 'victoire')

    for score in scores:
        print(f"Nom: {score['nom']}, Victoire: {score['victoire']}")
    return

def AfficherMeilleursScore():
    '''
    Affiche les 10 meilleurs Scores
    '''
    meilleurs_scores = ModelScore.objects.annotate(victoire=Count(Case(When(win="oui", then=1), output_field=IntegerField()))).order_by('-victoire')[:10].values('id', 'nom', 'victoire')

    for score in meilleurs_scores:
        print(f"Nom: {score['nom']}, Victoire: {score['victoire']}")
    return

