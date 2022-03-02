class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

if __name__ == '__main__':
    renzo = Pessoa(nome="Jose")
    p = Pessoa(renzo, nome= 'Luis')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print (p.nome, p.idade)
    for filho in p.filhos:
        print(filho.nome)
    p.sobrenome = 'Otavio'
    del p.filhos
    p.olhos = 1
    del p.olhos
    print(p.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(p.olhos)
    print(id(Pessoa.olhos), id(renzo.olhos), id(p.olhos))