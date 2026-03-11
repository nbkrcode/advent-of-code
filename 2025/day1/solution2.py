with open('input.txt', 'r') as f:
    texte = f.read().strip().split('\n')

def sol2():
    actuel=50
    compteur=0
    for rotation in texte:
        if rotation[0]=='L':
            for clic in range(int(rotation[1:])):
                actuel-=1
                if actuel==-1:
                    actuel=99
                if actuel==0:
                    compteur+=1
                
        else :
            for clic in range(int(rotation[1:])):
                actuel+=1
                if actuel==100:
                    actuel=0
                if actuel==0:
                    compteur+=1
    
    return compteur

print(sol2())