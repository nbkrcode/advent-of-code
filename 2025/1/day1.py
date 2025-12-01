with open('input.txt','r') as f:
    texte = f.read().strip().split('\n')

actuel = 50
r1=0
r2=0
for rotation in texte:
    if rotation[0]=='L':
        for _ in range(int(rotation[1:])):
            actuel-=1
            actuel=actuel%100
            if actuel==0:
                r2+=1
    else :
        for _ in range(int(rotation[1:])):
            actuel+=1
            actuel=actuel%100
            if actuel==0:
                r2+=1
    actuel=actuel%100
    if actuel == 0:
        r1+=1

print(r1)
print(r2)
