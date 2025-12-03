with open('input.txt','r') as f:
    texte = f.read().strip().split(',')

def isinvalid1(id):
    n=len(id)
    if n%2==1:
        return False
    for i in range(n//2):
        if id[i]!=id[i+n//2]:
            return False
    return True

def solution1():
    res=0
    for interval in texte:
        borne_inf,borne_sup=interval.split('-')
        n=int(borne_sup)-int(borne_inf)+1
        for i in range(n):
            id_actuel=int(borne_inf)+i
            id_actuel=str(id_actuel)
            if isinvalid1(id_actuel):
                res+=int(id_actuel)
    return res

print(solution1())

def isinvalid2(id):
    n=len(id)
    for L in range(1,n//2+1):
        if n%L==0:
            motif=id[:L]
            if motif * (n//L)==id:
                return True
            
    return False

def solution2():
    res=0
    for interval in texte:
        borne_inf,borne_sup=interval.split('-')
        n=int(borne_sup)-int(borne_inf)+1
        for i in range(n):
            id_actuel=int(borne_inf)+i
            id_actuel=str(id_actuel)
            if isinvalid2(id_actuel):
                res+=int(id_actuel)
    return res

print(solution2())