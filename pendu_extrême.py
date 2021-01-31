import time

def ouverturDico():
    dico=[]
    with open ("dico_fr.txt", 'r') as doss:
        lmots = doss.readlines()
    for mot in lmots:
        dico.append(mot[0:-1])
    return dico

def verifEntier(nbr):
    for x in nbr:
        if x not in ['0','1','2','3','4','5','6','7','8','9']:
            return 0
    return int(nbr)

def verifLetter(lettre,lettre_trouvee,lettre_essayee):
    if len(lettre) == 1:
        if lettre in ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']:
            if lettre not in lettre_trouvee:
                if lettre in lettre_essayee:
                    return True
                else:
                    print("Tu as déjà essayé cette lettre")
                    return False
            else:
                print("Vous avez déjà trouvé cette lettre")
                return False
        else:
            print("\nChoisissez une lettre qui se trouve dans l'alphabet")
            return False
    print("\nVous devez choisir seulement une lettre")
    return False

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

def lettre_commun(liste,lettre_trouvee):
    lettre_communes = []
    for lettre in liste[0]:
        if lettre not in lettre_communes and lettre not in lettre_trouvee:
            lettre_communes.append(lettre)

    for mot in liste[1:]:
        for lettre in lettre_communes:
            if lettre not in mot:
                lettre_communes.remove(lettre)
    return lettre_communes

def EverySame(ressemblance):
    for i in ressemblance:
        if i != 1:
            return False
    return True

def mot_a_choisir(liste,lettre):
    val = []
    liste2 = []
    for mot in liste:
        val.append(mot.count(lettre))

    minim = min(val)

    for mot in liste:
        if mot.count(lettre) == minim:
            liste2.append(mot)
    return liste2

def emplacementCommun(liste,lettre,lettre_trouvee):
    emplacement = [[] for x in range(len(liste))]
    liste2 = []
    ressemblance = [0 for x in range(len(liste))]
    for i,mot in enumerate(liste):
        for index,l in enumerate(mot):
            if l == lettre:
                emplacement[i].append(index)

    #print("emplacement",emplacement)
    for x in range(len(emplacement)):
        for ind in emplacement:
            if emplacement[x] == ind:
                ressemblance[x] += 1

    #print("ressemblance",ressemblance)
    if EverySame(ressemblance):
        liste2.append(liste[0])
        for p in range(len(emplacement[0])):
            g = emplacement[0][p]
            lettre_trouvee[g] = lettre
    else:
        fait = False
        maxi = max(ressemblance)
        for i in range(len(liste)):
            if ressemblance[i] == maxi:
                if not fait:
                    for p in range(len(emplacement[i])):
                        g = emplacement[i][p]
                        lettre_trouvee[g] = lettre
                    fait = True
                liste2.append(liste[i])
    return liste2, lettre_trouvee

def afficher_lettre_essayee(lettre_essayee):
    mot = "Vous n'avez pas essayé les lettres : "
    for i in lettre_essayee:
        mot += i+", "
    return mot

def afficher_mot(lettre_trouvee):
    mot = ''
    for x in lettre_trouvee:
        mot += x + " "
    return mot

def verifVic(lettre_trouvee):
    for l in lettre_trouvee:
        if l == "_":
            return False
    return True

#~~~~~~~~~~~~~~~~~~~~~~~~~~ Main ~~~~~~~~~~~~~~~~~~~~~~~~~~#
isInt = False
findWord = False
lettre_commune = []
lettre_essayee = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
coups = 0
dico = ouverturDico()

while not isInt:
    nbr = input("\nCombien de lettres voulez vous dans votre mot ? : ")
    nbr = verifEntier(nbr)
    if nbr < 2 or nbr > 20:
        print("Choisissez un nombre compris entre 2 et 20")
    else:
        isInt = True
    
lettre_trouvee = ["_" for x in range(nbr)]
possible = premier_tri(dico,nbr) #liste de mot à nbr lettres
lettre_commune = lettre_commun(possible,lettre_trouvee)

print("Laisser moi choisir un mot assez difficile à trouver ...")
time.sleep(2)
print("C'est bon, j'ai choisis mon mot ;)")

while not findWord:
    print(afficher_lettre_essayee(lettre_essayee))
    print(afficher_mot(lettre_trouvee))

    isCorrect = False
    while not isCorrect:
        lettre = input("Choisissez une lettre de l'alphabet : ")
        isCorrect = verifLetter(lettre,lettre_trouvee,lettre_essayee)

    if lettre in lettre_commune:
        possible = mot_a_choisir(possible,lettre)
        possible, lettre_trouvee = emplacementCommun(possible,lettre,lettre_trouvee)
    
    else:
        possible = trouver_lettre(possible,lettre)
    
    """
    if len(possible) <= 20:
        print(possible)
    """
    
    coups += 1
    lettre_essayee.remove(lettre)
    lettre_commune = lettre_commun(possible,lettre_trouvee)
    findWord = verifVic(lettre_trouvee)

print(afficher_mot(lettre_trouvee))
print(f"\nBravo vous avez trouvé mon mot en {coups} coups, c'est un peu nul")
input()