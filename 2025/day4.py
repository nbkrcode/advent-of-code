with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

W,H=len(texte[0]),len(texte)

def voisins(i,j,texte):
    voisins_temp=[(i-1,j-1),(i-1,j),(i-1,j+1),
                (i,j-1),(i,j+1),
                (i+1,j-1),(i+1,j),(i+1,j+1)]
    voisins=[]
    for (i,j) in voisins_temp:
        if 0<=i<H and 0<=j<W:
            voisins.append(texte[i][j])
    return(voisins)

def accessible(i,j,texte):
    compteur=0
    for e in voisins(i,j,texte):
        if e=='@':
            compteur+=1
    if compteur<4:
        return True
    return False

def solution1(texte):
    res=0
    for i in range(H):
        for j in range(W):
            if texte[i][j]=='@' and accessible(i,j,texte):
                res+=1
    return res

print(solution1(texte))

def solution2():
    texte_modif=texte.copy()
    removing_roll=True
    rolls_removed=0
    while removing_roll:
        if solution1(texte_modif)==0:
            removing_roll=False
        else:
            for i in range(H):
                for j in range(W):
                    if texte_modif[i][j]=='@' and accessible(i,j,texte_modif):
                        texte_modif[i]=texte_modif[i][:j]+'.'+texte_modif[i][j+1:]
                        rolls_removed+=1
    return rolls_removed


print(solution2())
