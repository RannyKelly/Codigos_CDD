class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.andando = False
        self.dormindo = False

    def dormir(self):
        if self.dormindo:
            print(f"{self.nome} já está dormindo.")
        else:
            self.dormindo = True
            print(f"{self.nome} está dormindo.")

    def pararDormir(self):
        if self.dormindo:
            self.dormindo = False
            print(f"{self.nome} parou de dormir.")
        else:
            print(f"{self.nome} não está dormindo.")

    def andar(self):
        if self.andando:
            print(f"{self.nome} já está andando.")
        else:
            self.andando = True
            print(f"{self.nome} está andando.")

    def pararAndar(self):
        if self.andando:
            self.andando = False
            print(f"{self.nome} parou de andar.")
        else:
            print(f"{self.nome} não está andando.")

    def comer(self):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
        else:
            self.comendo = True
            print(f"{self.nome} está comendo.")

    def pararComer(self):
        if self.comendo:
            self.comendo = False
            print(f"{self.nome} parou de comer.")
        else:
            print(f"{self.nome} não está comendo.")
