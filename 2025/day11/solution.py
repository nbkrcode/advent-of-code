import functools

with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

def output(ligne):
    sorties=ligne.split(':')[1]
    L=[]
    for e in sorties.split():
        L.append(e)
    return L

def device(ligne):
    return ligne.split(':')[0]

def cherche(machine):
    for i in range(len(texte)):
        if device(texte[i])==machine:
            return i

indice_you=cherche('you')

def parcours(i):
    res=0
    for sortie in output(texte[i]):
        if sortie=='out':
            res+=1
        else:
            res+=parcours(cherche(sortie))
    return res

print(parcours(indice_you))

@functools.cache
def parcours2(i,dac,fft):
    total=0
    a_parcourir=output(texte[i])
    for boutons in a_parcourir:
        if 'dac' in boutons:
            total+=parcours2(cherche(boutons),dac+1,fft)
        elif 'fft' in boutons:
            total+=parcours2(cherche(boutons),dac,fft+1)
        elif 'out' in boutons:
            if dac ==1 and fft==1:
                total+=1
        else:
            total += parcours2(cherche(boutons),dac,fft)
    return total

print(parcours2(cherche('svr'),0,0))

