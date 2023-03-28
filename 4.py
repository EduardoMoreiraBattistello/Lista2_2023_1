import random

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0
    
    def atualizar(self):
        dado = Dado(6)
        resultado = dado.rolar()
        
        self.pos += resultado
        
        if self.pos % 5 == 0:
            self.pos -= 1
        elif self.pos == 7 or self.pos == 17:
            self.pos += 2
        elif self.pos == 13:
            self.pos = 0
        
        if self.pos > 20:
            self.pos = 20
            self.vencedor = True
    
    def getPos(self):
        return self.pos
    
    def venceu(self):
        return self.pos == 20

class Dado:
    def __init__(self, num_faces):
        self.num_faces = num_faces
    
    def rolar(self):
        return random.randint(1, self.num_faces)

competidores = []
competidores.append(Competidor("Competidor 1"))
competidores.append(Competidor("Competidor 2"))
competidores.append(Competidor("Competidor 3"))
competidores.append(Competidor("Competidor 4"))
competidores.append(Competidor("Competidor 5"))

vencedor = None

while not vencedor:
    for competidor in competidores:
        competidor.atualizar()
        if competidor.venceu():
            vencedor = competidor
            break
    
    for competidor in competidores:
        print(competidor.nome, competidor.getPos())
    
print("O vencedor é", vencedor.nome)
