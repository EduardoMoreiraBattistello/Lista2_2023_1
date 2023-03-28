class CadastroCliente:
    def __init__(self, nome, sobrenome, data_nascimento, email, cpf, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.tentativas_incorretas = 0
        self.bloqueado = False
    
    def login(self, email, senha):
        if self.email == email and self.senha == senha:
            self.tentativas_incorretas = 0
            return True
        else:
            self.tentativas_incorretas += 1
            if self.tentativas_incorretas == 3:
                self.bloqueado = True
                print("Cadastro bloqueado por tentativas incorretas de login.")
            return False
    
    def get_nome(self):
        return self.nome
    
    def get_sobrenome(self):
        return self.sobrenome
    
    def get_data_nascimento(self):
        return self.data_nascimento
    
    def get_email(self):
        return self.email
    
    def get_cpf(self):
        return self.cpf
    
    def get_senha(self):
        return self.senha
    
    def is_bloqueado(self):
        return self.bloqueado

# criando um objeto CadastroCliente com os dados do cliente
cliente = CadastroCliente("Fulano", "de Tal", "01/01/2000", "fulano@gmail.com", "123.456.789-00", "senha123")

# realizando o login do cliente
email_login = input("Digite o seu email: ")
senha_login = input("Digite a sua senha: ")
if cliente.login(email_login, senha_login):
    print("Login realizado com sucesso!")
else:
    print("Email ou senha incorretos.")

# verificando se o cadastro está bloqueado
if cliente.is_bloqueado():
    print("Cadastro bloqueado por tentativas incorretas de login.")
else:
    # exibindo os dados do cliente
    print("Dados do cliente:")
    print("Nome completo:", cliente.get_nome(), cliente.get_sobrenome())
    print("Data de nascimento:", cliente.get_data_nascimento())
    print("Email:", cliente.get_email())
    print("CPF:", cliente.get_cpf())
    print("Senha:", cliente.get_senha())
