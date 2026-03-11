with open('input.txt', 'r') as f:
    texte = f.read().strip().split('\n')

def parcours(actuelle,cout,origine,compteur):
    H,W=len(texte),len(texte[0])
    x,y=actuelle
    if actuelle==(W-1,H-1):
        return cout
    
    neighbors_temp=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    neighbors=[]
    for e in neighbors_temp:
        if 0<=x<W and 0<=y<H and e!=origine:
            neighbors.append(e)
    return min(parcours(i,cout+int(texte[y][y]),(x,y),compteur+1) for i in neighbors)

print(parcours((0,0),0,None,0))