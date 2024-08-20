""" exercício de aplicação e criação de funções definidas"""

def saudacao(saudar):
    def saudacao2(nome):
     return f' {saudar}, {nome}!'
    return saudacao2

t1 = saudacao("bom dia")

for nome in ["maria", "joão", "Paulo"]:
    print(t1(nome))


print("dionisio", "santos", sep='.')


