with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

res1=0
for line in texte:
    n=len(line)
    best1=0
    best2=0
    indice_premier=0
    for i in range(n-1):
        if int(line[i])>int(best1):
            best1=line[i]
            indice_premier=i
    for i in range(indice_premier+1,n):
        if int(line[i])>int(best2):
            best2=line[i]
    res1+=int(best1+best2)

print(res1)