class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    p = Pessoa(renzo, nome= 'Luis')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print (p.nome, p.idade)
    for filho in p.filhos:
        print(filho.nome)
    p.sobrenome = 'Otavio'
    del p.filhos
    print(p.__dict__)
    print(renzo.__dict__)