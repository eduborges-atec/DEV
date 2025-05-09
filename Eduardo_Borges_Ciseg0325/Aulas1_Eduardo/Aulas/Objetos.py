class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def renovaridade(self,idade):
        self.idade = idade


Pessoas = []

for i in range(3):
    nom=input("Introduza o nome: ")    
    idad=input("Introduza a idade: ")
    Pessoas.append(Pessoa(nom,idad))
    print("Nome:" , Pessoas[i].nome)
    print("Idade:" , Pessoas[i].idade , "Anos")

novaidad=input("Introduza a nova idade: ")

Pessoas[i].renovaridade(novaidad)
print("Nome:" , Pessoas[i].nome)
print("Idade:" , Pessoas[i].idade , "Anos")
