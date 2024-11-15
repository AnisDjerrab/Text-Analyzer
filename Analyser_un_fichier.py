import re
import string
from collections import Counter
b = True
while b:
    print("")
    a = True
    while a:
        x = input("entrez le texte a analiser : ")
        if isinstance(x, str):
            a = False
            x = x.lower()
        else:
            print("ce doit etre un fichier texte pour qu'il soit analisé.")

    def nombre_de_mots(name):
        mots = re.findall(r"\w+", name)
        numbre_mots = len(mots)
        return numbre_mots
    nombre = nombre_de_mots(x)
    print(f"le nombre de mots que contient le texte est : {nombre}")

    def nombre_de_caracteres(name):
        mots = re.findall(r"\w", name)
        number_mots = len(mots)
        return number_mots
    number = nombre_de_caracteres(x)
    print(f"le nombre de caractres est : {number}")
    def nombre_de_consonnes_et_voyelles(name):
        lettres = re.findall(r"\w", name)
        nombre_voyelle = 0
        nombre_consonne = 0
        for lettre in lettres:
            if lettre in string.ascii_letters:
                if lettre in ["a", "e", "u", "i", "o"]:
                    nombre_voyelle += 1
                else:
                    nombre_consonne += 1
        consonnes_voyelles = ["le nombre de voyelle est de : ", "le nombre de consonne et de : "]
        consonnes_voyelles.insert(1, str(nombre_voyelle))
        consonnes_voyelles.insert(3, str(nombre_consonne))
        return consonnes_voyelles
    t = nombre_de_consonnes_et_voyelles(x)
    print(t)
            

    def lettre_la_plus(name):
        commun = Counter(name)
        plus_commun = commun.most_common(6)
        return plus_commun

    number = lettre_la_plus(x)
    print(f"voici donc une liste des caracteres les plus communs : {number}")

    def selectionner_par_longeur(name):
        mots_selectionnes = []
        for mot in name:
            if (len(mot) == 3 or len(mot) > 3) and mot not in ["les", "des", "une", "the", "they", "this", "who", "its"]:
                mots_selectionnes.append(mot)
        return mots_selectionnes
    
    def mot_le_plus_commun(name):
        mots = re.findall(r"\w+", name)
        mots = selectionner_par_longeur(mots)
        Compteur = Counter(mots)
        plus_communs = Compteur.most_common(6)
        plus_commun = Compteur.most_common(1)[0]
        plus_communs.append(("le mot le plus utilise est donc :", plus_commun))
        return plus_communs

    r = mot_le_plus_commun(x)
    print(f"les mots les plus communs sont {r}")
    print("")
    c = True
    while c:
        z = input("voulez vous entrer plus de texte (oui-non) : ")
        if isinstance(z, str):
            c = False
    if z.lower() == "oui":
        b = True
    else:
        b = False
    print("")