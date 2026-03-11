with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

coor=(0,0)
for x in range(len(texte[0])):
    if texte[0][x]=='S':
        coor=(x,0)
        break

def parcours(coor):
    x,y=coor
    res1=0
    res2=0
    a_traiter={(x,y+1):1}
    visited=set()
    visited.add((x,y+1))

    while a_traiter:

        prochain_a_traiter={}
        for (x_actuel,y_actuel),nb_timeline in a_traiter.items():
            if y_actuel>=len(texte):
                res2+=nb_timeline
                continue
            if not(0<=x_actuel<len(texte[0])):
                continue
            next_case=[]
            if texte[y_actuel][x_actuel] == '.':
                next_case.append((x_actuel,y_actuel+1))
            if texte[y_actuel][x_actuel] == '^':
                next_case.append((x_actuel-1,y_actuel))
                next_case.append((x_actuel+1,y_actuel))
                if (x_actuel, y_actuel) not in visited:
                    res1 += 1
                    visited.add((x_actuel, y_actuel))
            for case in next_case:
                if case not in prochain_a_traiter:
                    prochain_a_traiter[case] = 0
                prochain_a_traiter[case]+=nb_timeline
        a_traiter=prochain_a_traiter
    return res1,res2

print(parcours(coor)[0])

print(parcours(coor)[1])