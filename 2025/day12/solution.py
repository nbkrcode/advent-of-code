with open('input.txt','r') as f:
    texte=f.read().split('\n\n')

regions=texte[-1].strip().split('\n')

''' VERSION NAIVE QUI TOURNE A L'INFINI
old_shapes=[]
for e in texte[:-1]:
    shape=e.split(':')[1]
    shape=shape.strip().split('\n')
    old_shapes.append(shape)

def representation_shapes(shape): #shape de la forme ['###', '..#', '###']
    res=[]
    for i in range(3):
        for j in range(3):
            if shape[i][j]=='#':
                res.append((j,i))
    return res

shapes=[]
for shape in old_shapes:
    shapes.append(representation_shapes(shape))

def rotate(shape):
    new_shape=[]
    for coor in shape:
        x,y=coor
        temp=y
        y=x
        x=2-temp
        new_shape.append((x,y))
    new_shape.sort()
    return new_shape

def flip(shape):
    new_shape=[]
    for coor in shape:
        x,y=coor
        if x==0:
            x=2
        if x==2:
            x=0
        new_shape.append((x,y))
    new_shape.sort()
    return new_shape

rotations=[[] for _ in range(6)]
for i in range(len(shapes)):
    a=shapes[i]
    for _ in range(4):
        a=rotate(a)
        rotations[i].append(a)
    a=flip(shapes[i])
    for _ in range(4):
        a=rotate(a)
        rotations[i].append(a)

for k in range(len(rotations)):
    seen=[]
    for ori in rotations[k]:
        if ori not in seen:
            seen.append(ori)
    rotations[k]=seen

def peut_placer(grille, orientation, x0, y0):
    H = len(grille)
    L = len(grille[0])
    for x, y in orientation:
        if x0 + x >= L or y0 + y >= H:
            return False
        if grille[y0 + y][x0 + x] == '#':
            return False
    return True

def poser(grille, orientation, x0, y0, val):
    for x, y in orientation:
        grille[y0 + y][x0 + x] = val

counter=0

def backtracking(grille,formes_a_placer):
    global counter
    counter+=1
    if counter%10000==0:
        print('appels récursifs :',counter)
    if not formes_a_placer:
        return True
    
    indice_forme,nb=formes_a_placer[0]
    
    for orientation in rotations[indice_forme]:
        H = len(grille)
        L = len(grille[0])
        for y0 in range(H):
            for x0 in range(L):
                if peut_placer(grille,orientation,x0,y0):
                    poser(grille,orientation,x0,y0,'#')
                    nouvelles_formes=formes_a_placer.copy()
                    if nb == 1:
                        nouvelles_formes=nouvelles_formes[1:]
                    else:
                        nouvelles_formes[0]=(indice_forme,nb-1)
                    if backtracking(grille,nouvelles_formes):
                        return True
                    
                    poser(grille,orientation,x0,y0,'.')
    return False


# res=0
# for idx, region in enumerate(regions):
#     print(f"test de la region {idx+1}/{len(regions)}")
#     dim=region.split(':')[0]
#     L,H=int(dim.split('x')[0]),int(dim.split('x')[1])
#     grille=[['.' for _ in range(L)] for _ in range(H)]
#     formes_a_placer_temp=region.split(':')[1].split()
#     formes_a_placer=[]
#     for i in range(len(formes_a_placer_temp)):
#         formes_a_placer.append((i,int(formes_a_placer_temp[i])))
#     if backtracking(grille,formes_a_placer):
#         res+=1

'''

import sys
import time

# --- Partie 1 : Parsing (Identique) ---
# Remplace par ton ouverture de fichier réelle
with open('input.txt','r') as f:
    texte = f.read().split('\n\n')

regions = texte[-1].strip().split('\n')

shapes_data = {} 
for e in texte[:-1]:
    lines = e.strip().split('\n')
    idx = int(lines[0].replace(':', ''))
    coords = []
    for y, line in enumerate(lines[1:]):
        for x, char in enumerate(line):
            if char == '#':
                coords.append((x, y))
    shapes_data[idx] = coords

# Fonctions géométriques
def rotate(coords):
    return sorted([(y, 2-x) for x, y in coords])
def flip(coords): 
    return sorted([(2-x, y) for x, y in coords])
def normalize(coords):
    if not coords: return []
    min_x = min(c[0] for c in coords)
    min_y = min(c[1] for c in coords)
    return sorted([(x - min_x, y - min_y) for x, y in coords])

# Pré-calcul des variantes (Rotations/Flips)
all_variants = {}
for idx, coords in shapes_data.items():
    variants = set()
    current = coords
    for _ in range(4):
        variants.add(tuple(normalize(current)))
        current = rotate(current)
    current = flip(coords)
    for _ in range(4):
        variants.add(tuple(normalize(current)))
        current = rotate(current)
    all_variants[idx] = list(variants)

# Calcul de la surface (nombre de #) pour chaque forme
shape_areas = {idx: len(coords) for idx, coords in shapes_data.items()}

# --- Partie 2 : Moteur avec "Fail-Fast" ---

def solve_region(L, H, required_shapes):
    # 1. OPTIMISATION SURFACE : Si ça ne rentre pas mathématiquement, on arrête tout de suite
    total_gift_area = sum(shape_areas[sid] for sid in required_shapes)
    total_grid_area = L * H
    
    # Si les cadeaux sont plus grands que la boite -> Impossible
    if total_gift_area > total_grid_area:
        return False

    # 2. Génération des positions valides (Bitmasks)
    valid_moves = {}
    unique_ids = set(required_shapes)
    
    for sid in unique_ids:
        moves = []
        for variant in all_variants[sid]:
            w_shape = 0
            h_shape = 0
            if variant:
                w_shape = max(c[0] for c in variant) + 1
                h_shape = max(c[1] for c in variant) + 1
            
            if w_shape > L or h_shape > H: continue

            for dy in range(H - h_shape + 1):
                for dx in range(L - w_shape + 1):
                    mask = 0
                    for (x, y) in variant:
                        mask |= (1 << ((dy + y) * L + (dx + x)))
                    moves.append(mask)
        valid_moves[sid] = sorted(list(set(moves)))
        
        # Si une pièce requise ne peut pas rentrer du tout (0 positions), c'est fichu
        if not valid_moves[sid]:
            return False

    # 3. Tri intelligent des tâches
    # On trie d'abord par "nombre de possibilités" (le plus contraint en premier)
    # puis par taille (le plus gros en premier)
    required_shapes.sort(key=lambda sid: (len(valid_moves[sid]), -shape_areas[sid]))

    # 4. Backtracking
    def backtrack(idx, current_board, last_move_index):
        if idx == len(required_shapes):
            return True
        
        sid = required_shapes[idx]
        moves = valid_moves[sid]
        
        # Gestion des symétries (Doublons)
        start_i = 0
        if idx > 0 and required_shapes[idx] == required_shapes[idx-1]:
            start_i = last_move_index + 1
            
        for i in range(start_i, len(moves)):
            move = moves[i]
            if not (current_board & move):
                if backtrack(idx + 1, current_board | move, i):
                    return True
        return False

    return backtrack(0, 0, -1)

# --- Partie 3 : Exécution ---
print(f"Début du traitement de {len(regions)} régions...")
start_time = time.time()
res = 0

for i, region in enumerate(regions):
    if not region.strip(): continue
    
    # Affichage de progression tous les 10 items (ou chaque item si tu veux voir où ça bloque)
    if i % 10 == 0:
        print(f"Traitement région {i+1}/{len(regions)}... (Succès actuels: {res})")

    parts = region.split(':')
    dim_part = parts[0].split('x')
    L, H = int(dim_part[0]), int(dim_part[1])
    
    counts = list(map(int, parts[1].split()))
    required = []
    for s_idx, count in enumerate(counts):
        required.extend([s_idx] * count)
        
    if solve_region(L, H, required):
        res += 1

total_time = time.time() - start_time
print(f"\nTERMINE en {total_time:.2f} secondes.")
print(f"Nombre de régions valides : {res}")