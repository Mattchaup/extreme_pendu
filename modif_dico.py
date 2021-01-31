from random import*

def ouverturDico():
    dico=[]
    
    with open ("dico_fr.txt", 'r') as doss:
        lmots=doss.readlines()
    for mot in lmots:
        dico.append(mot[0:-1])
    return dico

def réecrire_dico(dico):
    with open ("dico_fr.txt",'w') as doss:
        for mots in dico:
            doss.write(f"{mots}\n")

def chercher_lettre_chelou(dico):
    lettre_chelou = []
    for mot in dico:
        for lettre in mot:
            if lettre not in ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']:
                if lettre not in lettre_chelou:
                    lettre_chelou.append(lettre)
    return lettre_chelou

def chercher_lettre_poss(dico,condition):
    mot_recherché = []
    for mot in dico:
        if mot[condition[0]] == condition[1]:
            mot_recherché.append(mot)
    return mot_recherché

def premier_tri(dico,nbr):
    liste = []
    for mot in dico:
        if len(mot)== nbr:
            liste.append(mot)
    return liste

def chercher_lettre(dico,lettre_recherchée):
    mot_recherché = []
    for mot in dico:
        for lettre in mot:
            if lettre == lettre_recherchée:
                if mot not in mot_recherché:
                    mot_recherché.append(mot)
    return mot_recherché

def modifier_lettre(dico,lettres_a_modif,nouv_lettre):
    print(dico[1])
    for mot in range (len(dico)):
        for lettres in (lettres_a_modif):
            dico[mot] = dico[mot].replace(lettres,nouv_lettre)
    print(dico[1])
    return dico

def jeuDuConnais(dico):
    trouver= ""
    coup = 0
    oui = 0

    while trouver != "stop":
        n = randint(0,len(dico))
        coup += 1
        trouver = input(f"Connaissez vous le mot {dico[n]} : ")
        if trouver == "o":
            oui += 1
        print(f"Votre ratio est de : {round(oui/coup,3)}")

def plusGrandMot(dico):
    max = 0
    for mot in dico:
        if len(mot) > max:
            max = len(mot)
    return max

def correctWord(mot):
    for lettre in mot:
        if lettre == " " or lettre == "'" or lettre == "." or lettre == "-":
            return False
    return True

dico = ouverturDico()
print(plusGrandMot(dico))
#poss = premier_tri(dico,8)

"""
condition = [[0,'a'],[2,'p'],[6,'r']]
for cond in condition:
    poss = chercher_lettre_poss(poss,cond)
print(poss)
"""

#poss = premier_tri(dico,5)
#poss = chercher_lettre_poss(poss,[3,'o'])
#print(dico.index('cheval'))
#print(chercher_lettre_chelou(dico))

"""#Supprime tout les mots avec des lettres_chelou
liste2 = []
for mot in dico:
    if correctWord(mot):
        liste2.append(mot)
"""

#print(chercher_lettre(dico,"."))
#dico = modifier_lettre(dico,[')','!'],'')
#réecrire_dico(liste2)
