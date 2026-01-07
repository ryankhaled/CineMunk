#Importation de tout les modules nécéssaires pour faire fonctionner les codes
from flask import Flask, render_template, request, redirect, url_for #le module flask pour faire tourner le server
import cinemunckdb as db #import le fichier python qui contient toutes les requetes sql 
from flask_wtf import FlaskForm #Nous permet de créer des forms pour insérer des informations dans notres bases de données à travers le site web
from wtforms import StringField, IntegerField, DateField, RadioField, SelectField
from wtforms.validators import DataRequired
import secrets
import os
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#Route pour la page d'acceuil
@app.route('/')
def home():
    # print()
    Serie = db.allSerie()
    #print(Serie)
    names=[]
    for i in Serie:
        names.append(i[1])
    return render_template("serie_hub.html", Serie=names)




#on crée un class MyForm pour pouvoir insérer des commentaires, elle sera utilisé pour @app.rout('/submit_commentaire')
class MyForm(FlaskForm):
    nom_commentaire = StringField('Votre commentaire', validators=[DataRequired()])
    idserie = SelectField('Les series', choices=[('1', "Jojo's Bizzare Adventures"), ('2', 'Initial D'), ('3', 'Stranger Things'), ('4', 'Brooklyn Nine-Nine'), ('5', 'The Walking Dead'), ('6', 'Lupin'), ('7', 'Wednesday'), ('8', 'Dirty Money'), ('9', 'The Circle of France'), ('10', 'Too Hot to Handle')], validators=[DataRequired()])

#Les routes des vues admins :
   
@app.route('/admin_Serie')
def Serie_de():
    Serie = db.allSerie()
    return render_template("liste_Serie.html", Serie=Serie)

@app.route('/admin_Saison')

def Saison_de():
    Saison = db.allSaison()
    return render_template("liste_Saison.html", Saison=Saison)

@app.route('/admin_Episode')
def Episode_de():
    Episode = db.allEpisode()
    return render_template("liste_Episode.html", Episode=Episode)

@app.route('/admin_Platforme')
def Platforme_de():
    Platforme = db.allPlatforme()
    return render_template("liste_Platforme.html", Platforme=Platforme)

@app.route('/admin_Personne')
def Personne_de():
    Personne = db.allPersonne()
    return render_template("liste_Personne.html", Personne=Personne)


@app.route('/admin_Genre')
def Genre_de():
    Genre = db.allGenre()
    return render_template("liste_Genre.html", Genre=Genre)


@app.route('/admin_Fonction')
def Fonction_de():
    Fonction = db.allFonction()
    return render_template("liste_Fonction.html", Fonction=Fonction)

@app.route('/admin_Commentaire')
def Commentaire_de():
    Commentaire = db.allCommentaire()
    return render_template("liste_Commentaire.html", Commentaire=Commentaire)



@app.route('/admin_hub')
def home_admin():
    return render_template("les_admins.html")


#Les routes des vues complexe :

@app.route('/Jojo')
def jojo_saison_name():
    Jojo = db.jojo_saison()
    return render_template("jojo.html", Jojo=Jojo)


@app.route('/platforme_payant')
def platforme_payant():
    payant = db.payant()
    return render_template("platforme_payant.html", payant=payant)  

@app.route('/serie_platforme')
def serie_platforme():
    serplat = db.serie_platforme()
    return render_template("serie_platforme.html", serplat=serplat) 

@app.route('/nbserie_gratuit')
def nb_serie_gratuit():
    sergrat = db.nbserie_gratuit()
    return render_template("nbserie_gratuit.html", sergrat=sergrat) 


#On utilise la methode 'GET', 'POST' pour faire fonctionner le formulaire pour les commentaires
@app.route('/submit_commentaire', methods=['GET', 'POST'])
def add_comment():
    form = MyForm() #on intègre MyForm de la classe créé en début de code
    if form.validate_on_submit():
        nom_commentaire = form.nom_commentaire.data
        idserie = form.idserie.data
        max_id = db.get_max_id_commentaire() #db._get_max_id_commentaire nous renvoye une valeur dans un tuple c'est pour ça que max_id[0][0] est mit sur cette forme
        id = max_id[0][0] + 1 #max_id + 1 sera le id du nouveau commentaire ajouté par l'utilisateur 
        #print(max_id[0][0])
        print(f"INSERT INTO Commentaire (idcommentaire, nomcommentaire, idserie) VALUES ({id}, {nom_commentaire}, {idserie})") #Les nouvelles valeurs pour {id}, {nom_commentaire} et {idserie} seront ajouté dans la base de donnée grâce à la requette sql dans le f string
        comment_added = db.new_comment(id, nom_commentaire, idserie)
        print(comment_added)
        return redirect(url_for('add_comment'))
    
    return render_template("add_comment.html", form=form) #On identifie le template qui contient le code html pour complémenter ce code python




    
#Un deuxième hub moin jolie utilisé en cas de problème

@app.route('/serie_hub2')
def serie_hub2():
    return render_template('serie_hub2.html')


#Les routes pour les vues "jolies" et plus complexe. Ces pages sont présentes sur la page d'acceuil, c'est les pages avec les images

@app.route('/les_series')
def les_series():
    serie= db.serie()
    return render_template('les_series.html', serie=serie)

@app.route('/les_personnes')
def les_personnes():
    personne= db.personne()
    return render_template('les_personnes.html', personne=personne)

@app.route('/les_episodes')
def les_episodes():
    episode= db.episode()
    return render_template('les_episodes.html', episode=episode)

@app.route('/les_saisons')
def les_saisons():
    ssaison= db.saison()
    return render_template('les_saisons.html', ssaison=ssaison)


@app.route('/les_platformes')
def les_platformes():
    platforme= db.platforme()
    return render_template('les_platformes.html', platforme=platforme)



if __name__ == "__main__":
    print('Running the flask app')
    app.run(debug=True, port=8080) #Le port de base 5500 ne fonctionnait pas donc on a choisi 8080
