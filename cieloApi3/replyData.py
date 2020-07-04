# coding=utf-8
class ReplyData(object):

    def __init__(self):

        # Combinação de códigos que indicam erro no endereço de cobrança e/ou entrega.
        # Os códigos são concatenados usando o caractere ^.
        self.address_info_code = None

        # Combinação de códigos que indicam o score do pedido.
        # Os códigos são concatenados usando o caractere ^.
        self.factor_code = None

        # Score total calculado para o pedido. Vai de 0 - 100 - Quanto mais elevado, maior o risco.
        self.score = None

        # Sigla do país de origem da compra.
        self.bin_country = None

        # Nome do banco ou entidade emissora do cartão.
        self.card_issuer = None

        # Tipo da bandeira
        self.card_scheme = None

        # Nível de risco do domínio de e-mail do comprador, de 0 a 5,
        # onde 0 é risco indeterminado e 5 representa o risco mais alto.
        self.host_severity = None

        # Sequência de códigos que indicam que existe uma excessiva alteração
        # de identidades do comprador. Os códigos são concatenados usando o caractere ^.
        self.internet_info_code = None

        # Tipo de roteamento de IP utilizado pelo computador.
        self.ip_routing_method = None

        # Nome do modelo de score utilizado.
        self.score_model_used = None

        # Caso o lojista seja assinante do Enhanced Case Management,
        # ele recebe este valor com o nível de prioridade, sendo 1 o mais alto e 5 o mais baixo.
        self.case_priority = None
