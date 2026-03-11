with open('input.txt', 'r') as f:
    texte = f.read().strip().split('\n')

def parcours(debut,sens,texte):
    x,y=debut
    dx,dy=sens
    H=len(texte)
    W=len(texte[0])
    visited = set()
    a_traiter=[(x,y,dx,dy)]
    while len(a_traiter)!=0:
        x_actuel,y_actuel,dx,dy=a_traiter.pop(0)

        while True:

            if not (0<=x_actuel<W and 0<=y_actuel<H):
                break

            case_actuelle=(x_actuel,y_actuel,dx,dy)
            if case_actuelle in visited:
                break

            visited.add(case_actuelle)

            case = texte[y_actuel][x_actuel]
            if case=='.':
                pass

            elif case=='/':
                dx,dy=-dy,-dx

            elif case=='\\':
                dx,dy=dy,dx

            elif case=='-':
                if dy!=0:
                    a_traiter.append((x_actuel,y_actuel,1,0))
                    a_traiter.append((x_actuel,y_actuel,-1,0))
                    break

            elif case=='|':
                if dx !=0:
                    a_traiter.append((x_actuel,y_actuel,0,1))
                    a_traiter.append((x_actuel,y_actuel,0,-1))
                    break
            
            x_actuel+=dx
            y_actuel+=dy
    hashtag=set((x,y) for x,y,_,_ in visited)
    resultat = len(hashtag)

    return resultat
        
print(parcours((0,0),(1,0),texte))