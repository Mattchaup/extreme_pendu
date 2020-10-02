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

def chercher_lettre(dico,lettre_recherchée):
    mot_recherché = []
    for mot in dico:
        for lettre in mot:
            if lettre == lettre_recherchée:
                mot_recherché.append(mot)
    return mot_recherché

def modifier_lettre(dico,lettres_a_modif,nouv_lettre):
    print(dico[1])
    for mot in range (len(dico)):
        for lettres in (lettres_a_modif):
            dico[mot] = dico[mot].replace(lettres,nouv_lettre)
    print(dico[1])
    return dico

dico = ouverturDico()
#print(dico.index('cheval'))
#print(chercher_lettre_chelou(dico))
#print(chercher_lettre(dico,'cheval'))
#dico = modifier_lettre(dico,[')','!'],'')
#réecrire_dico(dico)
