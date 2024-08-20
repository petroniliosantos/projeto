import random  
Ordem = 1
for _ in range(10):
    numeros1 = [14,20,18,22,6,24,16]
    numeros2 = [2,4,8,10,12]
    numeros3_i = [1,3,5,25,7,15]
    numeros4_i = [17,21,9,23,19,13,11]
    random.shuffle(numeros1)
    random.shuffle(numeros2)
    random.shuffle(numeros3_i)
    random.shuffle(numeros4_i)
    sorteio1 = sorted(numeros1[0:3])
    sorteio2 = sorted(numeros2[0:4])
    sorteio3 = sorted(numeros3_i[0:4])
    sorteio4 = sorted(numeros4_i[0:4])
    soma_sorteio = sorted(sorteio1 + sorteio2 + sorteio3 + sorteio4)
    '''print(f"Jogo {Ordem}",soma_sorteio)'''
    print(soma_sorteio)
    '''Ordem += 1''' 






