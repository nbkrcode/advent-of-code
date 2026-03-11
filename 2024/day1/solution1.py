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

print(distance)