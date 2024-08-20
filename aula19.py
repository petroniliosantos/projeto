import random  
Ordem = 1
for _ in range(3168):
    '''numeros1 = [1,3,5,7,9,11,13,15,17,19,21,23,25]
    numeros2 = [2,4,6,8,10,12,14,16,18,20,22,24]'''
    numeros1 = [4,8,12,22]
    numeros2 = [1,7,15,17,19,21]
    fixo1 = [2,6,10,14,16,18,20,24]
    fixo2 = [3,5,9,11,13,23,25]
    random.shuffle(numeros1)
    random.shuffle(numeros2)
    random.shuffle(fixo1)
    random.shuffle(fixo2)
    sorteio1 = sorted(numeros1[0:2])
    sorteio2 = sorted(numeros2[0:4])
    sorteio3 = sorted(fixo1[0:5])
    sorteio4 = sorted(fixo2[0:4])
    soma_sorteio = sorted(sorteio1 + sorteio2 + sorteio3 + sorteio4)
    '''print(f"Jogo {Ordem}",soma_sorteio)'''
    print(soma_sorteio)
    Ordem += 1  