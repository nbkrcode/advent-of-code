data = open('input.txt','r')
texte = data.read()
games=texte.split('\n')
games.pop()

def lvl1(games):
        
    d={'red':12,'blue':14,'green':13}
    id_total = (100*101)/2
    mauvais_id = 0

    for game in games:
        num,match=game.split(':')
        num = int(num.split(' ')[1]) #numéro game
        sous_match=match.split(';') 
        liste_colors=[]
        for m in sous_match:
            colors=m.split(',')
            liste_colors.append(colors)
        
        mauvais = False
        for sous_match in liste_colors:
            for colors in sous_match:
                colors=colors.strip()
                nbr,couleur=colors.split()
                if int(nbr)>d[couleur]:
                    mauvais=True
                    break
            if mauvais:
                break
        if mauvais:
            mauvais_id+=num
    return(int(id_total-mauvais_id))

print(lvl1(games))