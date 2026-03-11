with open('input.txt', 'r') as f:
    texte = f.read().strip().split('\n')

def sol1():
    actuel=50
    compteur=0
    for rotation in texte:
        if rotation[0]=='L':
            actuel-=int(rotation[1:])
        else :
            actuel+=int(rotation[1:])
        
        while actuel>=100:
            actuel-=100
        while actuel<0:
            actuel+=100
        if actuel == 0:
            compteur+=1
    return compteur

print(sol1())