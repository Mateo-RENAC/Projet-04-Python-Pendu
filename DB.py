import mysql.connector

def CreerLaBaseDeDonnee():
    '''
    Fonction permettant de créer une base de donnée avec 3 tables.

    Table utilisateur :
    -id_use INT AUTO_INCREMENT PRIMARY KEY
    -nom_use VARCHAR(20)
    
    Table Mot :
    -id_Mot INT AUTO_INCREMENT PRIMARY KEY
    -mot varchar(25)

    Table Score :
    -id_Score INT AUTO_INCREMENT PRIMARY KEY
    -id_use_FK INT FOREIGN KEY(utilisateur)
    -Result varchar(9) ENUM('Victoire','Défaite')
    -Diffuculté varchar(10) ENUM('Facile','Moyen','Difficile')
    -Date DATETIME
    '''
    # Se connecter à MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CESI2024"
    )

    # Créer une base de données
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS PenduDatabase")

    # Utiliser la base de données
    cursor.execute("USE PenduDatabase")

   # Créer la table Utilisateur
    cursor.execute("""CREATE TABLE IF NOT EXISTS Utilisateur (
                    id_use INT AUTO_INCREMENT PRIMARY KEY,
                    nom_use VARCHAR(20)
                )""")

# Créer la table Mot
    cursor.execute("""CREATE TABLE IF NOT EXISTS Mot (
                    id_Mot INT AUTO_INCREMENT PRIMARY KEY,
                    mot VARCHAR(25)
                )""")

# Créer la table Score
    cursor.execute("""CREATE TABLE IF NOT EXISTS Score (
                    id_Score INT AUTO_INCREMENT PRIMARY KEY,
                    id_use_FK INT,
                    Result ENUM('Victoire','Défaite'),
                    Difficulte ENUM('Facile','Moyen','Difficile'),
                    Date DATETIME,
                    FOREIGN KEY (id_use_FK) REFERENCES Utilisateur(id_use)
                )""")
    
# Fermer la connexion
    conn.close()
    return

CreerLaBaseDeDonnee()