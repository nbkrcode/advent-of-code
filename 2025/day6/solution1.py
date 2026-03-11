with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

symboles=texte[-1].split()
nombres_temp=texte[:-1]
nombres=[]
for nombre in nombres_temp:
    nombres.append(nombre.strip().split())


res1=0
for i in range(len(symboles)):
    res_colonne=0
    for j in range(len(nombres)):
        if symboles[i]=='+':
            res_colonne+=int(nombres[j][i])
        else:
            if res_colonne==0:
                res_colonne=1
                res_colonne=res_colonne*int(nombres[j][i])
            else:
                res_colonne=res_colonne*int(nombres[j][i])

    res1+=res_colonne

print(res1)


                