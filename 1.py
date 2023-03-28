import random

class Dado:
    def __init__(self, num_faces):
        self.num_faces = num_faces
    
    def rolar(self):
        return random.randint(1, self.num_faces)

# Instanciando um dado com 6 faces
dado_6_faces = Dado(6)
print(f"Jogando o dado de 6 faces:")
for i in range(3):
    resultado = dado_6_faces.rolar()
    print(f"Jogada {i+1}: {resultado}")

# Instanciando um dado com 8 faces
dado_8_faces = Dado(8)
print(f"\nJogando o dado de 8 faces:")
for i in range(3):
    resultado = dado_8_faces.rolar()
    print(f"Jogada {i+1}: {resultado}")

# Instanciando um dado com 12 faces
dado_12_faces = Dado(12)
print(f"\nJogando o dado de 12 faces:")
for i in range(3):
    resultado = dado_12_faces.rolar()
    print(f"Jogada {i+1}: {resultado}")
