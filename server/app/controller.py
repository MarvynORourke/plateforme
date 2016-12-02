import db

def add_course(id_user, name, texte):
    ident = db.add_course(id_user, name)
    fichier = open("static/" + ident, 'w')
    fichier.write(texte)
    fichier.close()
    
