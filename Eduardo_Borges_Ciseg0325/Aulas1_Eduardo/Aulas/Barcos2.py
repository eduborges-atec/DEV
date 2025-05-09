import time

class Barco:
    def __init__(self, marca, potencia, ano, nos):
        self.marca = marca
        self.potencia = potencia
        self.ano = ano
        self.nos = nos
        self.ligado = False
        self.farois = False

    def ligarBarco(self):
        if not self.ligado:
            self.ligado = True
            print("O barco foi ligado.")
        else:
            print("O barco já está ligado.")

    def desligarBarco(self):
        if self.ligado:
            self.ligado = False
            self.farois = False
            self.nos = 0
            print("O barco foi desligado.")
        
    def ligarFarois(self):
        if self.ligado:
            if not self.farois:
                self.farois = True
                print("Faróis ligados.")

    def desligarFarois(self):
        if self.farois:
            self.farois = False
            print("Faróis desligados.")

    def Acelera(self, nivel):
        if self.ligado:
            if nivel == 1:
                self.nos += 2
            if nivel == 2:
                self.nos += 5
            if nivel == 3:
                self.nos += 10

    def Abranda(self, nivel):
        if self.ligado:
            if nivel == 1:
                self.nos = max(0, self.nos - 2)
            if nivel == 2:
                self.nos = max(0, self.nos - 5)
            if nivel == 3:
                self.nos = max(0, self.nos - 10)

Barco1 = Barco("Yamaha", "200cv", 2024, 0)

Barco1.ligarBarco()
Barco1.ligarFarois()
print("Nos:", Barco1.nos)
Barco1.Acelera(1)
time.sleep(1)
print("Nos:", Barco1.nos)
Barco1.Acelera(2)
time.sleep(1)
print("Nos:", Barco1.nos)
Barco1.Abranda(1)
print("Nos:", Barco1.nos)
time.sleep(1)
Barco1.Abranda(2)
print("Nos:", Barco1.nos)
Barco1.desligarFarois()
Barco1.desligarBarco()

    
