import sqlite3
from datetime import datetime


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

def CompterVictoires():
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

