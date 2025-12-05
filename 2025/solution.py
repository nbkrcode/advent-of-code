with open('input.txt','r') as f:
    texte = f.read().strip().split('\n')

indice_milieu=0
for i in range(len(texte)):
    if texte[i]=='':
        indice_milieu=i

intervals=texte[:indice_milieu]
numbers=texte[indice_milieu+1:]

def isfresh(number):
    for interval in intervals:
        borne_inf,borne_sup=interval.split('-')
        if int(borne_inf)<=int(number)<=int(borne_sup):
            return True
    return False

def solution1():
    res1=0
    for number in numbers:
        if isfresh(number):
            res1+=1
    return res1
print(solution1())

def solution2():
    new=[]
    for interval in intervals:
        debut,fin=interval.split('-')
        debut,fin=int(debut),int(fin)
        new.append((debut,fin))
    new.sort()
    finals=[]
    debut,fin=new[0]
    for i in range(1,len(new)):
        next_deb,next_fin=new[i]
        if next_deb<=fin:
            fin=max(fin,next_fin)
        else:
            finals.append((debut,fin))
            debut,fin=next_deb,next_fin
    finals.append((debut,fin))
    res2=0
    for (debut,fin) in finals:
        res2+= (fin-debut+1)
    return res2
print(solution2())