from solution1 import parcours

with open('input.txt', 'r') as f:
    texte = f.read().strip().split('\n')

def opti():
    H,W=len(texte),len(texte[0])
    best=0
    for y in range(H):
        if parcours((0,y),(1,0),texte)>best:
            best=parcours((0,y),(1,0),texte)
        if parcours((W-1,y),(-1,0),texte)>best:
            best=parcours((W-1,y),(-1,0),texte)
    for x in range(W):
        if parcours((x,0),(0,1),texte)>best:
            best=parcours((x,0),(0,1),texte)
        if parcours((x,H-1),(0,-1),texte)>best:
            best=parcours((x,H-1),(0,-1),texte)
    return best

print(opti())