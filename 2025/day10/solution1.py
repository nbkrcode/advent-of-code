with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')

def tuple_to_list(b):
    b=b.strip("()")
    if b=='':
        return []
    return [int(x) for x in b.split(',')]

def solution():
    res=0

    for machine in texte: #on parcourt chaque ligne donc chaque machine
        separe=machine.strip().split()
        lumieres=separe[0].strip("[]") # de la forme .##.#..
        boutons=separe[1:-1] # de la forme ['(1,2,3)', '(0,2,3)']

        # Construction target
        target = '' 
        for i in range(len(lumieres)):
            if lumieres[i]=='.':
                target+='0'
            else:
                target+='1'
        target=int(target,2)

        # Construction masques
        masks=[]
        for b in boutons:
            mask=''
            indices=tuple_to_list(b)
            for i in range(len(lumieres)):
                if i in indices:
                    mask+='1'
                else:
                    mask+='0'
            masks.append(int(mask,2)) 

        # Parcours en largeur
        queue=[(0,0)] 
        visited=set()
        visited.add(0)
        head=0
        while head<len(queue):
            state,dist=queue[head]
            head+=1
            if state==target:
                res+=dist
                break
            for mask in masks:
                new_state = state ^ mask
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state,dist+1))
    return res

print(solution())