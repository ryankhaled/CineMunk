import sqlite3 #On import sqlite3 pour pouvoir effectuer des requêtes sql dans python

DBNAME = "Cinemunck.db" #On import notre base de donnée 

def _select(requete, params=None):
    """ Exécute une requête type select"""
    with sqlite3.connect(DBNAME) as db: #Cette ligne établit une connection avec notre fichier Cinemunck.db
        c = db.cursor()
        if params is None:
            c.execute(requete)
        else: #Les lignes 10 et 12 verifient s'il existe des paramètres à prendre en question lors de la requête sql
            c.execute(requete, params)
        res = c.fetchall() #fetchall va chercher tout les résultats d'une colonne lors d'une requête sql
    return res

#Les requêtes pour les vues admins :

def allSerie():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT idserie, nomserie, datesortie, episodetotale, nbsaison, idgenre FROM Serie") #On a tout selectionner manuellement
    rows = cursor.fetchall()
    conn.close()
    return rows


def allSaison():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Saison") #On a utilisé * pour tout selectionner automatiquement
    rows = cursor.fetchall()
    conn.close()
    return rows



def allEpisode():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Episode")
    rows = cursor.fetchall()
    print(rows) #Certaine fonction on des #print(rows) qui eu on été utilisé pour vérifier le fonctionnement de la requête
    conn.close()
    return rows

def allPlatforme():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Platforme")
    rows = cursor.fetchall()
    #print(rows)
    conn.close()
    return rows

def allPersonne():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Personne")
    rows = cursor.fetchall()
    #print(rows)
    conn.close()
    return rows




def allGenre():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Genre")
    rows = cursor.fetchall()
    #print(rows)
    conn.close()
    return rows

def allFonction():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Fonction")
    rows = cursor.fetchall()
    #print(rows)
    conn.close()
    return rows

def allCommentaire():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Commentaire")
    rows = cursor.fetchall()
    #print(rows)
    conn.close()
    return rows

#Les requêtes pour les vues complexes 

def jojo_saison():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nomserie, nomsaison FROM Serie Inner Join saison On Serie.idserie=saison.idserie Where nomserie like 'JoJo%'") #On effectue une jointure entre la table Serie et Saison pour afficher toutes les saisons de la serie "Jojo's Bizzare Adventures"
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

def payant():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("Select nomplatforme, prix from Platforme where prix = 'Payant'") #Cette requête affiche tout les platformes payantes
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

def serie_platforme():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nomserie, nomplatforme FROM serie inner join platforme on serie.idplatforme=Platforme.idplatforme where prix = 'Gratuit'") #Cette requête contient une jointure entre la table Serie et Platforme pour afficher toutes les Serie disponible sur des platformes gratuites
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

def nbserie_gratuit():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*)FROM SERIE INNER JOIN Platforme ON SERIE.idplatforme=Platforme.idplatforme WHERE prix='Gratuit' UNION SELECT nomserie FROM Serie INNER JOIN Platforme ON SERIE.idplatforme=Platforme.idplatforme WHERE prix='Gratuit'")
    #Cette requête affiche le nombre de serie gratuite ainsi que le nom de ces série avec un Count, deux Inner Join et un Union Select
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

import sqlite3

def new_comment(idcommentaire, nomcommentaire, idserie): #les arguments de la fonction son défini car cette fonction est celle en charge de modifier la base de donnée à travers le site flask
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Commentaire (idcommentaire, nomcommentaire, idserie) VALUES (?, ?, ?)", (idcommentaire, nomcommentaire, idserie))
    # (?,?,?) à ses point d'intérogation défini en ordre par idcommentaire, nomcommentaire et idserie qui eux sont déterminé dans project_db_flask.py et add_comment.html (par l'utilisateur)
    conn.commit() #effectue des changement à la base de donnée
    conn.close()
    return True #renvoi True si ça fonctionne, comme moyen de vérification

   
def get_max_id_commentaire(): #renvoie le plus grand idcommentaire pour que le nouveau commentaire ajouté par l'utilisateur soit max_id + 1
    conn =sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("select max(idcommentaire) from Commentaire")
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

def menu_serie():
    conn =sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("select idserie from Serie")
    rows = cursor.fetchall()
    print(rows)
    return rows


#Requête de vue complexe :


def personne():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("Select idpersonne, nompersonne, naissance, nomfonction, urlpersonne from Personne INNER JOIN Fonction on Personne.idfonction=Fonction.idfonction") 
    #Cette requête est une jointure entre la table Personne et Fonction afin d'attribuer la fonction (acteur, réalisateur, actrice) d'une personne sur le site flask dans /les_personnes
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows
   

def serie():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT idserie, nomserie, datesortie, episodetotale, nbsaison, nomgenre, nomplatforme, urlserie FROM SERIE INNER JOIN Platforme ON SERIE.idplatforme=Platforme.idplatforme INNER JOIN Genre ON SERIE.idgenre=Genre.idgenre")
    #Un double inner join pour afficher le nom de la platforme de la serie et le nom du genre de la serie sur la page /les_series
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

def episode():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT idepisode, nomepisode, dateepisode, nomserie, nomsaison, urlserie FROM Episode INNER JOIN Serie ON Episode.idserie=Serie.idserie INNER JOIN Saison ON Episode.idsaison=Saison.idsaison")
    #Un double inner join pour afficher le nom d'un épisode, le nom de la serie et la saison à la qu'elle elle appartient. /les_episodes
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows


def saison():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT idsaison, nomsaison, nbepisode, nomserie, urlserie from Saison Inner join Serie on saison.idserie=Serie.idserie")
    #Un inner join pour relier la table Saison à Serie pour attribuer la saison à sa série. /les_saison
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows


def platforme():
    conn = sqlite3.connect('Cinemunck.db')
    cursor = conn.cursor()
    cursor.execute("SELECT idplatforme, nomplatforme, prix, urlplatforme FROM Platforme") # /les_platformes
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows






