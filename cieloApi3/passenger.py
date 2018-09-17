# coding=utf-8
class Passenger(object):

    def __init__(self):

        # Email do Passageiro
        self.email = None

        # Id do passageiro a quem o bilheite foi emitido.
        self.identity = None

        # Nome do passageiro.
        self.name = None

        # Classificação do Passageiro.
        self.rating = None

        # Número do telefone do passageiro. Para pedidos fora do U.S.,
        # a CyberSource recomenda que inclua o código do país.
        self.phone = None

        # Classificação da empresa aérea. Pode-se usar valores como Gold ou Platina.
        self.status = None


