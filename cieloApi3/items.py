# coding=utf-8
class Items(object):

    def __init__(self):

        # Campo que avaliará os endereços de cobrança e
        # entrega para difrentes cidades, estados ou países.
        self.gift_category = None

        # Nível de importância do e-mail e endereços IP dos clientes em risco de pontuação.
        self.host_hedge = None

        # Nível dos testes realizados sobre os dados do comprador com pedidos recebidos sem sentido.
        self.non_sensical_hedge = None

        # Não	Nível de obscenidade dos pedidos recebedidos.
        self.obscenities_hedge = None

        # Nível dos testes realizados com os números de telefones.
        self.phone_hedge = None

        # Nome do Produto.
        self.name = None

        # Quantidade do produto a ser adquirido.
        self.quantity = None

        # Código comerciante identificador do produto.
        self.sku = None

        # Preço unitário do produto.
        self.unit_price = None

        # Nível do risco do produto.
        self.risk = None

        # Nível de importância da hora do dia do pedido do cliente.
        self.time_hedge = None

        # Tipo do produto.
        self.type = None

        # Nível de importância de frequência de compra do cliente.
        self.velocity_hedge = None

        # Objeto com os dados do passageiro
        self.passenger = None

