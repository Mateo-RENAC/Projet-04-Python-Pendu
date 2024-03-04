import sqlite3
from datetime import datetime
import random


def ObtenirMotAleatoire(niveau_difficulte):
    '''Sélectionne aléatoirement un mot depuis 
    la base de données en fonction du niveau de difficulté'''
    # Se connecter à la base de données
    conn = sqlite3.connect("PenduDatabase.db")
    cursor = conn.cursor()

    # Sélectionner un mot aléatoire en fonction du niveau de difficulté
    if niveau_difficulte == 'Facile':
        cursor.execute("SELECT mot FROM Mot WHERE LENGTH(mot) <= 6 ORDER BY RANDOM() LIMIT 1")
    elif niveau_difficulte == 'Moyen':
        cursor.execute("SELECT mot FROM Mot WHERE LENGTH(mot) > 6 AND LENGTH(mot) <= 8 ORDER BY RANDOM() LIMIT 1")
    elif niveau_difficulte == 'Difficile':
        cursor.execute("SELECT mot FROM Mot WHERE LENGTH(mot) > 8 ORDER BY RANDOM() LIMIT 1")
    else:
        raise ValueError("Niveau de difficulté invalide. Les valeurs valides sont 'Facile', 'Moyen' et 'Difficile'.")

    # Récupérer le mot sélectionné aléatoirement
    mot = cursor.fetchone()[0]

    # Fermer la connexion
    conn.close()

    return mot


def CreerLaBaseDeDonnee():
    '''
    Fonction permettant de créer une base de données avec 3 tables.

    Table utilisateur :
    -id_use INTEGER PRIMARY KEY AUTOINCREMENT
    -nom_use VARCHAR(20)
    
    Table Mot :
    -id_Mot INTEGER PRIMARY KEY AUTOINCREMENT
    -mot VARCHAR(25)

    Table Score :
    -id_Score INTEGER PRIMARY KEY AUTOINCREMENT
    -id_use_FK INT
    -Result TEXT CHECK (Result IN ('Victoire', 'Défaite'))
    -Difficulte TEXT CHECK (Difficulte IN ('Facile', 'Moyen', 'Difficile'))
    -Date DATETIME,
    '''
    # Se connecter à SQLite
    conn = sqlite3.connect("PenduDatabase.db")
    cursor = conn.cursor()

    # Créer la table Utilisateur
    cursor.execute("""CREATE TABLE IF NOT EXISTS Utilisateur (
                    id_use INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom_use VARCHAR(20)
                )""")

    # Créer la table Mot
    cursor.execute("""CREATE TABLE IF NOT EXISTS Mot (
                    id_Mot INTEGER PRIMARY KEY AUTOINCREMENT,
                    mot VARCHAR(25)
                )""")

    # Créer la table Score
    cursor.execute("""CREATE TABLE IF NOT EXISTS Score (
                    id_Score INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_use_FK INT,
                    Result TEXT CHECK (Result IN ('Victoire', 'Défaite')),
                    Difficulte TEXT CHECK (Difficulte IN ('Facile', 'Moyen', 'Difficile')),
                    Date DATETIME,
                    FOREIGN KEY (id_use_FK) REFERENCES Utilisateur(id_use)
                )""")
    
    # Fermer la connexion
    conn.close()
    return 'CREATE_DATABASE_SUCCESS'


def SauvegarderScore(Pseudo, Resultat, Difficulte):
    '''Sauvegarde les Scores avec pour paramètre le nom du joueur,
    le résultat de la partie (Victoire ou défaite) et enfin la difficulté'''
    # Se connecter à la base de données
    conn = sqlite3.connect("PenduDatabase.db")
    cursor = conn.cursor()

    # Insérer l'utilisateur s'il n'existe pas
    cursor.execute("INSERT OR IGNORE INTO Utilisateur (nom_use) VALUES (?)", (Pseudo,))

    # Récupérer l'ID de l'utilisateur
    cursor.execute("SELECT id_use FROM Utilisateur WHERE nom_use = ?", (Pseudo,))
    id_utilisateur = cursor.fetchone()[0]

    # Insérer le score
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO Score (id_use_FK, Result, Difficulte, Date) VALUES (?, ?, ?, ?)",
                   (id_utilisateur, Resultat, Difficulte, date))

    # Commit et fermer la connexion
    conn.commit()
    conn.close()
    return 'SAVE_SUCCESS'


def AfficherScoresBase():
    '''Affiche les Scores des joueurs'''
    # Se connecter à la base de données
    conn = sqlite3.connect("PenduDatabase.db")
    cursor = conn.cursor()

    # Compter le nombre de victoires pour chaque utilisateur
    cursor.execute("""SELECT Utilisateur.nom_use, COUNT(Score.id_Score) AS Victoires
                    FROM Utilisateur
                    LEFT JOIN Score ON Utilisateur.id_use = Score.id_use_FK
                    WHERE Score.Result = 'Victoire'
                    GROUP BY Utilisateur.id_use""")

    # Afficher le résultat
    for row in cursor.fetchall():
        print("Nom:", row[0], "| Nombre de victoires:", row[1])

    # Fermeture de la connexion
    conn.close()
    

def AfficherScoresAlphabetique():
    '''Affiche les scores des joueurs ordonnés 
    par ordre alphabétique des noms d'utilisateur'''
    # Se connecter à la base de données
    conn = sqlite3.connect("PenduDatabase.db")
    cursor = conn.cursor()

    # Sélectionner les noms d'utilisateur et le nombre de victoires
    cursor.execute("""SELECT Utilisateur.nom_use, COUNT(Score.id_Score) AS Victoires
                    FROM Utilisateur
                    LEFT JOIN Score ON Utilisateur.id_use = Score.id_use_FK
                    WHERE Score.Result = 'Victoire'
                    GROUP BY Utilisateur.id_use
                    ORDER BY Utilisateur.nom_use""")

    # Afficher le résultat
    for row in cursor.fetchall():
        print("Nom:", row[0], "| Nombre de victoires:", row[1])

    # Fermer la connexion
    conn.close()


def AfficherScoresParScoreDecroissant():
    '''Affiche les scores chaque joueur ordonnés
    par le nombre de victoires en ordre décroissant'''
    # Se connecter à la base de données
    conn = sqlite3.connect("PenduDatabase.db")
    cursor = conn.cursor()

    # Sélectionner les noms d'utilisateur et le nombre de victoires, ordonnés par nombre de victoires en ordre décroissant
    cursor.execute("""SELECT Utilisateur.nom_use, COUNT(Score.id_Score) AS Victoires
                    FROM Utilisateur
                    LEFT JOIN Score ON Utilisateur.id_use = Score.id_use_FK
                    WHERE Score.Result = 'Victoire'
                    GROUP BY Utilisateur.id_use
                    ORDER BY Victoires DESC""")

    # Afficher le résultat
    for row in cursor.fetchall():
        print("Nom:", row[0], "| Nombre de victoires:", row[1])

    # Fermer la connexion
    conn.close()


def AfficherPartiesParDifficulte():
    '''Affiche les parties de chaque joueur ordonnées par niveau de difficulté (Difficile, Moyen, Facile)'''
    # Se connecter à la base de données
    conn = sqlite3.connect("PenduDatabase.db")
    cursor = conn.cursor()

    # Sélectionner les noms d'utilisateur, le nombre de parties et la difficulté, ordonnés par niveau de difficulté
    cursor.execute("""SELECT Utilisateur.nom_use, 
                             SUM(CASE WHEN Score.Difficulte = 'Difficile' THEN 1 ELSE 0 END) AS Parties_Difficile,
                             SUM(CASE WHEN Score.Difficulte = 'Moyen' THEN 1 ELSE 0 END) AS Parties_Moyen,
                             SUM(CASE WHEN Score.Difficulte = 'Facile' THEN 1 ELSE 0 END) AS Parties_Facile
                      FROM Utilisateur
                      LEFT JOIN Score ON Utilisateur.id_use = Score.id_use_FK
                      GROUP BY Utilisateur.nom_use
                      ORDER BY Utilisateur.nom_use""")

    # Afficher le résultat
    for row in cursor.fetchall():
        print("Nom:", row[0], "| Parties Difficiles:", row[1], "| Parties Moyennes:", row[2], "| Parties Faciles:", row[3])

    # Fermer la connexion
    conn.close()


def RemplirTableMotDepuisFichier(nom_fichier):
    '''Remplit la table Mot à partir d'un fichier texte'''
    # Se connecter à la base de données
    conn = sqlite3.connect("PenduDatabase.db")
    cursor = conn.cursor()

    # Ouvrir le fichier texte et insérer chaque mot dans la table Mot
    with open(nom_fichier, 'r') as file:
        mots = file.readlines()
        for mot in mots:
            cursor.execute("INSERT INTO Mot (mot) VALUES (?)", (mot.strip(),))

    # Commit et fermer la connexion
    conn.commit()
    conn.close()