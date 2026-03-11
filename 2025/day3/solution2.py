with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

def solution2(ligne):
    n=len(ligne)
    indice_debut=0
    res_ligne='0'
    for k in range(12):
        best=0
        for i in range(indice_debut,n-(11-k)):
            if int(ligne[i])>int(best):
                best=ligne[i]
                indice_debut=i+1
        res_ligne+=best
    return(res_ligne[1:])

res2=0
for ligne in texte:
    res2+=int(solution2(ligne))

print(res2)