with open('input.txt','r') as f:
    texte=f.read().strip().split('\n')



for machine in texte:
    separe=machine.strip().split()
    boutons=separe[1:-1]
    target=separe[-1].strip('{}')
    target_list=target.split(',')
    boutons_list=[[0 for i in range(len(target_list))] for j in range(len(boutons))]
    

