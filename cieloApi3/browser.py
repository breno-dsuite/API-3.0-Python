# ecoding=utf-8
class Browser(object):

    def __init__(self):

        # Booleano para identificar se o browser do cliente aceita cookies.
        self.cookies_accepted = None

        # E-mail registrado no browser do comprador.
        # Obrigatorio
        self.email = None

        # Nome do host onde o comprador estava antes de entrar no site da loja.
        self.host_name = None

        # Endereco IP do comprador. eh altamente recomendavel o envio deste campo.
        self.ip_address = None

        # Nome do browser utilizado pelo comprador.
        self.type = None