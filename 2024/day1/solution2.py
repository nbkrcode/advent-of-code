data = open('input.txt','r')
texte = data.read()


l1=[]
l2=[]

lignes = texte.split('\n')
lignes.pop()

for ligne in lignes:
    l1.append((ligne.split('   '))[0])
    l2.append((ligne.split('   '))[1])

l1.sort()
l2.sort()

distance=0
for i in range(len(l1)):
    distance+=abs(int(l1[i])-int(l2[i]))


d = {}

for e in l2:
    if e in d:
        d[e]+=1
    else:
        d[e]=1

r2=0

for e in l1:
    if e in d:
        r2+=int(e)*int(d[e])

print(r2)

