data = open('input.txt','r')
texte = data.read()
games=texte.split('\n')
games.pop()

def lvl2(games):
    somme=0
    for game in games:
        tete,contenu=game.split(':')
        num=tete.split()[1]
        subsets=contenu.strip().split(';')
        d={'blue':0,'red':0,'green':0}
        power=0
        for e in subsets:
            colors=e.split(',')
            for c in colors:
                if int(c.strip().split()[0])>(d[c.strip().split()[1]]):
                    d[c.strip().split()[1]]=int(c.strip().split()[0])
        power=d['blue']*d['red']*d['green']
        somme+=power
    return somme
        
        
print(lvl2(games))

        

