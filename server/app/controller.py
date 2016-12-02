import db

def add_course(id_user, name, texte):
    ident = db.add_course(id_user, name)
    fichier = open("./app/static/cours/" + str(ident), 'w')
    fichier.write(texte)
    fichier.close()
    
