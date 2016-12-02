import db

def add_course(id_user, name, texte):
    ident = add_course(id_user,name)
    fichier = open("static"+"/" + name + ident, "w")
    fichier.write(texte)
    
