# coding=utf-8
class Travel(object):

    def __init__(self):

        #Data, hora e minuto de partida do vôo.
        self.departure_time = None

        # Tipo de viagem.
        self.journey_type = None

        # Rota da viagem. Concatenação de pernas de viagem individuais no formato ORIG1- DEST1.
        self.route = None

        # Códigos dos Aeroportos.
        self.legs = None
