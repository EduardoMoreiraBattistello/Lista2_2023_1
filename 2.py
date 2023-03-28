class Calculadora:
    
    def somar(self, num1, num2):
        return num1 + num2
    
    def subtrair(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        if num2 == 0:
            print("Erro: divisão por zero!")
            return -1
        else:
            return num1 / num2

# criando uma instância da classe Calculadora
calc = Calculadora()

# realizando operações com a calculadora
print("5 + 3 =", calc.somar(5, 3))
print("5 - 3 =", calc.subtrair(5, 3))
print("5 * 3 =", calc.multiplicar(5, 3))
print("5 / 3 =", calc.dividir(5, 3))
print("5 / 0 =", calc.dividir(5, 0))
