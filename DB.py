import sqlite3

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

CreerLaBaseDeDonnee()