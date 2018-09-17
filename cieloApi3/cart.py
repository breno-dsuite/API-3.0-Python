# coding=utf-8
class Cart(object):

    def __init__(self):

        # Booleano que indica se o pedido é para presente ou não.
        self.is_gift = None

        # Booleano que define se devoluções são aceitas para o pedido.
        self.returns_acapted = None

        # Lista de Objetos que correspondem aos Itens do carrinho
        self.items = None