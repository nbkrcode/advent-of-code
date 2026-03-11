from math import sqrt

with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

n = len(texte)

def distance(p,q): #distance eucli entre p et q
    p_coords = p.split(",")
    q_coords = q.split(",")
    p1,p2,p3=int(p_coords[0]),int(p_coords[1]),int(p_coords[2])
    q1,q2,q3=int(q_coords[0]),int(q_coords[1]),int(q_coords[2])
    return sqrt((p1-q1)**2+(p2-q2)**2+(p3-q3)**2)

connexions=[]
for i in range(n):
    for j in range(i+1,n):
        dist=distance(texte[i],texte[j])
        connexions.append((dist,i,j))
connexions.sort() 

rep=[i for i in range(n)] #à la base chaque élément est seul dans son circuit donc rep[i]=i
taille=[1]*n

def union(x,y):
    cx=rep[x]
    cy=rep[y]
    if cx!=cy:
        for i in range(len(rep)):
            if rep[i]==cy:
                rep[i]=cx
        taille[cx]+=taille[cy]
        taille[cy]=0

for _ in range(1000):
    _, i, j = connexions.pop(0)
    union(i, j)

taille.sort()

print(taille[-1]*taille[-2]*taille[-3])

# PARTIE 2

connexions=[]
for i in range(n):
    for j in range(i+1,n):
        dist=distance(texte[i],texte[j])
        connexions.append((dist,i,j))
connexions.sort() 

rep=[i for i in range(n)]
taille=[1]*n

def nb_non_nul(liste):
    compteur=0
    for e in liste:
        if e!=0:
            compteur+=1
    return compteur

L=[]
while nb_non_nul(taille)>1:
    _, i, j = connexions.pop(0)
    union(i, j)
    L.append((texte[i],texte[j]))

#print(L)



x1=texte[i].split(',')[0]
x2=texte[j].split(',')[0]
print(int(x1)*int(x2))

# print(distance("86151,65474,45150", "86173,71010,39505"))
# print(distance("86151,65474,45150", "85690,65926,40929"))
# print(distance("45219,24392,68485","45189,23896,68216"))
