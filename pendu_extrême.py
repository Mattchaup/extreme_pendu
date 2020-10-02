import random

def ouverturDico():
    dico=[]

    with open ("dico_fr.txt", 'r') as doss:
        lmots=doss.readlines()
    for mot in lmots:
        dico.append(mot[0:-1])
    return dico

def verifEntier(nbr):
    for x in nbr:
        if x not in ['0','1','2','3','4','5','6','7','8','9']:
            return 0
    return int(nbr)

def premier_tri(dico,nbr):
    liste = []
    for mot in dico:
        if len(mot)== nbr:
            liste.append(mot)
    return liste

def trouver_lettre(liste,lettre):
    possible = []
    for mot in liste:
        if lettre not in mot:
            possible.append(mot)
    return possible

def lettre_commun(liste):
    lettre_communes = [lettre for lettre in liste[0]]
    for mot in liste:
        for lettre in lettre_communes:
            if lettre not in mot:
                lettre_communes.remove(lettre)
    if len(lettre_communes) > 0:
        return False
    else:
        return True

def minim_lettre(liste,lettre):
    val = []
    for mot in liste:
        valMot = 0
        for x in mot:
            if x == lettre:
                valMot += 1
        val.append(valMot)
    print(val)


def afficher_mot(possible,nbr):
    mot = ''
    for x in range (nbr):
        mot += '_ '
    return mot

#Main
isInt = False
findWord = False
dico = ouverturDico()

while not isInt:
    nbr = input("\nCombien de lettres voulez vous dans votre mot ? : ")
    nbr = verifEntier(nbr)
    if nbr < 2 or nbr > 24:
        print("Choisissez un nombre compris entre 2 et 24")
    else:
        isInt = True

possible = premier_tri(dico,nbr)
while not findWord:
    if lettre_commun(possible):
        lettre = input("Tappez une lettre : ")
    else:
        print(possible)
        word = random.choice(possible)
        findWord = True
    possible = trouver_lettre(possible,lettre)
    print(len(possible))
    print(afficher_mot(possible,nbr))

print(word)