class Pessoa(object):

    def __init__(self, nome):
        self.nome = nome


class Empregado(Pessoa):

    def __init__(self, nome, cargo):

        super().__init__(nome)
        self.cargo = cargo
