with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

def surface(a,b):
    xa,ya=a.split(',')
    xb,yb=b.split(',')
    xa,xb,ya,yb=int(xa),int(xb),int(ya),int(yb)
    return (abs(xa-xb)+1)*(abs(ya-yb)+1)

max_surface=0

for a in texte:
    for b in texte:    
        if surface(a,b)>max_surface:
            max_surface=surface(a,b)

print(max_surface)

#-- PART 2 --

V,H=[],[] #lignes verticales et horizontales
for i in range(len(texte)):
    x1,y1=texte[i].split(',')
    x2,y2=texte[(i+1)%len(texte)].split(',')
    x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)
    if x1==x2:
        V.append(((x1,y1),(x2,y2)))
    else:
        H.append(((x1,y1),(x2,y2)))


def valide(rect):
    a,b=rect
    x1,y1=a.split(',')
    x2,y2=b.split(',')
    x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)

    #ligne verticale
    for (x,ya),(_,yb) in V:
        if (xmin < x < xmax) and not (max(ya,yb) <= ymin or min(ya,yb) >= ymax):
            return False
        
    #ligne horizontale
    for (xa,y),(xb,_) in H:
        if (ymin < y <ymax) and not (max(xa,xb) <= xmin or min(xa,xb) >= xmax):
            return False
    return True

max_surface2=0
for a in texte:
    for b in texte:
        if a != b:
            s = surface(a, b)
            if s > max_surface2 and valide((a, b)):
                max_surface2 = s

print(max_surface2)

