with open('input.txt','r') as f:
    texte=f.read().split('\n')

symboles=texte[-1].split()
nombres=texte[:-1]

longueur_max=0 
for ligne in nombres:
    if len(ligne)>longueur_max:
        longueur_max=len(ligne)

grille_padded = []
for ligne in nombres:
    ligne_padded=ligne + ' '*(longueur_max-len(ligne))
    grille_padded.append(ligne_padded)

resultats_colonnes = []
bloc_travail = []
indice_symbole = 0

for indice_colonne in range(longueur_max): #on parcourt chaque colonne de la grille paddée
    
    colonne_verticale = []
    for ligne in grille_padded:
        colonne_verticale.append(ligne[indice_colonne]) #ici on a notre colonne de largeur 1 et d'indice indice_colonne
    #on vérifie si c'est une colonne d'espace (qui sépare deux colonnes de nombres)
    est_separateur = True
    for c in colonne_verticale:
        if c != ' ':
            est_separateur = False
            break
            
    if est_separateur: #si c'est une colonne d'espace, on calcule le résultat du bloc de travail qui précède
        
        if bloc_travail: #si on a un bloc de nombre qui est formé (les nombres sont dans leur bonne forme)            
            r = 0
            if symboles[indice_symbole] == '+':
                r = 0
                for nombre in bloc_travail:
                    r += nombre
            elif symboles[indice_symbole] == '*':
                r = 1
                for nombre in bloc_travail:
                    r *= nombre
            resultats_colonnes.append(r)
            
            indice_symbole += 1 #on passe au symbole d'après
            
            bloc_travail = [] #on réinitialise le bloc
        continue

    # Sinon si c'est une colonne de chiffres, on forme le nouveau terme
    
    nombre_str = ""
    for caractere in colonne_verticale:
        if '0' <= caractere <= '9':
            nombre_str += caractere
            
    if nombre_str: #si le terme formé n'est pas vide
        bloc_travail.append(int(nombre_str)) #on le rajoute au bloc

#pour le dernier bloc qui n'a pas de séparateur ensuite
if bloc_travail:
    
    r = 0
    if symboles[indice_symbole] == '+':
        r = 0
        for nombre in bloc_travail:
            r += nombre
    elif symboles[indice_symbole] == '*':
        r = 1
        for nombre in bloc_travail:
            r *= nombre
            
    resultats_colonnes.append(r)

res2 = 0
for resultat in resultats_colonnes:
    res2 += resultat
    
print(res2)