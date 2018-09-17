# coding=utf-8
class FraudAnalysis(object):

    def __init__(self):

        # Tipo de Fluxo para realização da analise de fraude. Padrao: AuthorizeFirst
        self.sequence = None

        # Criterio do fluxo. Padrão: OnSuccess - Só realiza a analise se tiver sucesso na transação/analise.
        self.sequence_criteria = None

        # Identificador utilizado para cruzar informacoes obtidas pelo Browser do internauta com os dados enviados para analise.
        # Este mesmo valor deve ser passado na variavel SESSIONID do script do DeviceFingerPrint.
        self.finger_print_id = None

        # Objeto que identifica os dados do Browser
        self.browser = None

        # Objeto que identifica os dados do carrinho
        self.cart = None

        # Lista de Objetos que tem informacoes adicionais
        self.merchant_definid_fields = None

        # Objeto com dados da entrega
        self.shipping = None

        # Objeto com dados da viajem aerea
        self.travel = None

        # Indentificação da Transação no Antifraud.
        self.id = None

        # Status da Transação.
        self.status = None

        # Dados da Análise
        self.reply_data = None

        # Veio no retorno, sem informação na documentação
        self.is_retry_transaction = None

        # Veio no retorno, sem informação na documentação
        self.total_order_amount = None

