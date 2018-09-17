# API-3.0-Python

SDK API-3.0 Python Cielo



* [Principais recursos](#principais-recursos)
* [Limitações](#limitações)
* [Exemplos](#exemplos)
    * [Criando um pagamento com cartão de crédito](#criando-um-pagamento-com-cartão-de-crédito)
    * [Criando um pagamento recursivo com cartão de crédito](#criando-um-pagamento-recursivo-com-cartão-de-crédito)
    * [Criando um agendamento de pagamento recursivo com cartão de crédito](#criando-um-agendamento-de-pagamento-recursivo-com-cartão-de-crédito)
    * [Gerando token de cartão de crédito e criando um pagamento com o token](#gerando-token-de-cartão-de-crédito-e-criando-um-pagamento-com-o-token)
    * [Gerando um boleto simples](#gerando-um-boleto-simples)
    * [Gerando um boleto completo](#gerando-um-boleto-completo)
* [Manual Oficial da Cielo](#manual-oficial-da-cielo)

## Principais recursos

* [x] Pagamentos por cartão de crédito.
* [x] Pagamentos recorrentes.
    * [x] Com autorização na primeira recorrência.
    * [x] Com autorização a partir da primeira recorrência.
* [x] Pagamentos por cartão de débito.
* [x] Pagamentos por boleto (Bradesco e Banco do Brasil).
* [ ] Pagamentos por transferência eletrônica.
* [x] Cancelamento de autorização.
* [x] Consulta de pagamentos.
* [x] Análise de fraude.

## Limitações

Por envolver a interface de usuário da aplicação, o SDK funciona apenas como um framework para criação das transações. Nos casos onde a autorização é direta, não há limitação; mas nos casos onde é necessário a autenticação ou qualquer tipo de redirecionamento do usuário, o desenvolvedor deverá utilizar o SDK para gerar o pagamento e, com o link retornado pela Cielo, providenciar o redirecionamento do usuário.

## Utilizando o SDK
Para criar um pagamento simples com cartão de crédito com o SDK, basta fazer:

## Instalação
O API-3.0 Python Cielo pode ser facilmente instalado com o comando a seguir:
```bash
pip install cieloApi3
```

## Exemplos
### Criando um pagamento com cartão de crédito

```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('123')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Fulano de Tal')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '0000000000000001'
credit_card.holder = 'Fulano de Tal'

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(15700)
sale.payment.credit_card = credit_card

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer sua captura,
# se ela não tiver sido capturada ainda
response_capture_sale = cielo_ecommerce.capture_sale(payment_id, 15700, 0)
print '----------------------response_capture_sale----------------------'
print json.dumps(response_capture_sale, indent=2)
print '----------------------response_capture_sale----------------------'

# E também podemos fazer seu cancelamento, se for o caso
response_cancel_sale = cielo_ecommerce.cancel_sale(payment_id, 15700)
print '---------------------response_cancel_sale---------------------'
print json.dumps(response_cancel_sale, indent=2)
print '---------------------response_cancel_sale---------------------'
```


### Criando um pagamento recursivo com cartão de crédito
```python

from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('789')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador accept')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('262', 'Visa')
credit_card.expiration_date = '03/2019'
credit_card.card_number = '1234123412341231'
credit_card.holder = 'Teste Holder'

recurrent_payment = RecurrentPayment()
recurrent_payment.interval = INTERVAL_SEMIANNUAL
recurrent_payment.end_date = '2019-12-01'

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(1500)
sale.payment.recurrent_payment = recurrent_payment
sale.payment.credit_card = credit_card

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'



# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer sua captura,
# se ela não tiver sido capturada ainda
response_capture_sale = cielo_ecommerce.capture_sale(payment_id, 15700, 0)
print '----------------------response_capture_sale----------------------'
print json.dumps(response_capture_sale, indent=2)
print '----------------------response_capture_sale----------------------'

# E também podemos fazer seu cancelamento, se for o caso
response_cancel_sale = cielo_ecommerce.cancel_sale(payment_id, 15700)
print '---------------------response_cancel_sale---------------------'
print json.dumps(response_cancel_sale, indent=2)
print '---------------------response_cancel_sale---------------------'



# Com a venda recorrente criada na Cielo, já temos o ID do pagamento recorrente
recurrent_payment_id = sale.payment.recurrent_payment.recurrent_payment_id

# Consulta informações da venda recorrente
response_get_recurrent_payment = cielo_ecommerce.get_recurrent_payment(recurrent_payment_id)
print '---------------------response_get_recurrent_payment---------------------'
print json.dumps(response_get_recurrent_payment, indent=2)
print '---------------------response_get_recurrent_payment---------------------'
```


### Criando um agendamento de pagamento recursivo com cartão de crédito
```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('789')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador rec programada')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('262', 'Visa')
credit_card.expiration_date = '03/2019'
credit_card.card_number = '1234123412341231'
credit_card.holder = 'Teste Holder'

recurrent_payment = RecurrentPayment(False)
recurrent_payment.interval = INTERVAL_SEMIANNUAL
recurrent_payment.start_date = '2015-06-01'
recurrent_payment.end_date = '2019-12-01'

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(1500)
sale.payment.recurrent_payment = recurrent_payment
sale.payment.credit_card = credit_card

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'
```

### Gerando token de cartão de crédito e criando um pagamento com o token
```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '4532117080573700'
credit_card.holder = 'Comprador T Cielo'
credit_card.customer_name = 'Comprador Teste Cielo'

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_card_token = cielo_ecommerce.create_card_token(credit_card)
print '----------------------response_create_card_token----------------------'
print json.dumps(response_create_card_token, indent=2)
print '----------------------response_create_card_token----------------------'

# Com o cartão gerado token na Cielo, já temos o Token do cartão para uma futura cobrança
new_card_token = credit_card.card_token
print 'New Card Token:', new_card_token

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('456')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Credit Card utilizando os dados de teste via token
credit_card_token = CreditCard('123', 'Visa')
credit_card_token.card_token = new_card_token

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(100)
sale.payment.credit_card = credit_card_token

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'
```

### Gerando um boleto simples
```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('333')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(15700)
sale.payment.type = PAYMENTTYPE_BOLETO

sale.payment.provider = PROVIDER_BRADESCO

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer uma consulta do pagamento
response_get_sale = cielo_ecommerce.get_sale(payment_id)
print '----------------------response_get_sale----------------------'
print json.dumps(response_get_sale, indent=2)
print '----------------------response_get_sale----------------------'

print '\r\nLink Boleto:', sale.payment.url, '\r\n'
```

### Gerando um boleto completo
```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('555')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Payment informando o valor do pagamento
payment = Payment(15700)
payment.type = PAYMENTTYPE_BOLETO

payment.provider = PROVIDER_BANCO_DO_BRASIL
payment.address = 'Rua Alegria N: 3 Bairro: Rosa São Paulo-SP'
payment.boleto_number = '123'
payment.assignor = 'Empresa Teste'
payment.demonstrative = 'Demonstrativo Teste'
payment.expiration_date = '2017-06-11'
payment.identification = '11884926754'
payment.instructions = 'Aceitar somente até a data de vencimento, após essa data juros de 1% dia.'

sale.payment = payment

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer uma consulta do pagamento
response_get_sale = cielo_ecommerce.get_sale(payment_id)
print '----------------------response_get_sale----------------------'
print json.dumps(response_get_sale, indent=2)
print '----------------------response_get_sale----------------------'

print '\r\nLink Boleto:', sale.payment.url, '\r\n'
```

### Criando um pagamento com análise de fraude
```python
# coding=utf-8
from cieloApi3 import *
import json

"""
Exemplo de envio de JSON com a classe Sale com o Analisador de Fraudes 
{  
   "MerchantOrderId":"201411173454307",
   "Customer":{  
      "Name":"Comprador crédito AF",
      "Email":"compradorteste@live.com",
      "Birthdate":"1991-01-02",
      "Address":{  
         "Street":"Rua Júpter",
         "Number":"174",
         "Complement":"AP 201",
         "ZipCode":"21241140",
         "City":"Rio de Janeiro",
         "State":"RJ",
         "Country":"BRA"
      },
      "DeliveryAddress":{  
         "Street":"Rua Júpter",
         "Number":"174",
         "Complement":"AP 201",
         "ZipCode":"21241140",
         "City":"Rio de Janeiro",
         "State":"RJ",
         "Country":"BRA"
      }
   },
   "Payment":{  
     "Type":"CreditCard",
     "Amount":100,
     "Currency":"BRL",
     "Country":"BRA",
     "ServiceTaxAmount":0,
     "Installments":1,
     "SoftDescriptor":"123456789ABCD",
     "Interest":"ByMerchant",
     "Capture":false,
     "Authenticate":false,
     "CreditCard":{  
         "CardNumber":"4024007197692931",
         "Holder":"Teste accept",
         "ExpirationDate":"12/2030",
         "SecurityCode":"023",
         "Brand":"Visa"
     },
     "FraudAnalysis":{
       "Sequence":"AuthorizeFirst",
       "SequenceCriteria":"OnSuccess",
       "FingerPrintId":"074c1ee676ed4998ab66491013c565e2",
       "Browser":{
         "CookiesAccepted":false,
         "Email":"compradorteste@live.com",
         "HostName":"Teste",
         "IpAddress":"200.190.150.350",
         "Type":"Chrome"
        },
       "Cart":{
         "IsGift":false,
         "ReturnsAccepted":true,
         "Items":[{
           "GiftCategory":"Undefined",
           "HostHedge":"Off",
           "NonSensicalHedge":"Off",
           "ObscenitiesHedge":"Off",
           "PhoneHedge":"Off",
           "Name":"ItemTeste",
           "Quantity":1,
           "Sku":"201411170235134521346",
           "UnitPrice":123,
           "Risk":"High",
           "TimeHedge":"Normal",
           "Type":"AdultContent",
           "VelocityHedge":"High",
           "Passenger":{
             "Email":"compradorteste@live.com",
             "Identity":"1234567890",
             "Name":"Comprador accept",
             "Rating":"Adult",
             "Phone":"999994444",
             "Status":"Accepted"
            }
           }]
       },
       "MerchantDefinedFields":[{
            "Id":95,
            "Value":"Eu defini isso"
        }],
        "Shipping":{
            "Addressee":"Sr Comprador Teste",
            "Method":"LowCost",
            "Phone":"21114740"
        },
        "Travel":{
            "DepartureTime":"2010-01-02",
            "JourneyType":"Ida",
            "Route":"MAO-RJO",
          "Legs":[{
                "Destination":"GYN",
                "Origin":"VCP"
          }]
        }
     }
  }
}

Exemplo de retorno quando usado o AF
{
    "MerchantOrderId": "201411173454307",
    "Customer": {
        "Name": "Comprador crédito AF",
        "Email": "compradorteste@live.com",
        "Birthdate": "1991-01-02",
        "Address": {
            "Street": "Rua Júpter",
            "Number": "174",
            "Complement": "AP 201",
            "ZipCode": "21241140",
            "City": "Rio de Janeiro",
            "State": "RJ",
            "Country": "BRA"
        },
        "DeliveryAddress": {
            "Street": "Rua Júpter",
            "Number": "174",
            "Complement": "AP 201",
            "ZipCode": "21241140",
            "City": "Rio de Janeiro",
            "State": "RJ",
            "Country": "BRA"
        }
    },
    "Payment": {
        "ServiceTaxAmount": 0,
        "Installments": 1,
        "Interest": "ByMerchant",
        "Capture": false,
        "Authenticate": false,
        "CreditCard": {
            "CardNumber": "402400******2931",
            "Holder": "Teste accept",
            "ExpirationDate": "12/2030",
            "SaveCard": false,
            "Brand": "Visa"
        },
        "ProofOfSale": "492115",
        "Tid": "10069930692606D31001",
        "AuthorizationCode": "123456",
        "SoftDescriptor":"123456789ABCD",
        "FraudAnalysis": {
            "Sequence": "AuthorizeFirst",
            "SequenceCriteria": "OnSuccess",
            "FingerPrintId": "074c1ee676ed4998ab66491013c565e2",
            "MerchantDefinedFields": [
                {
                    "Id": 95,
                    "Value": "Eu defini isso"
                }
            ],
            "Cart": {
                "IsGift": false,
                "ReturnsAccepted": true,
                "Items": [
                    {
                        "Type": "AdultContent",
                        "Name": "ItemTeste",
                        "Risk": "High",
                        "Sku": "201411170235134521346",
                        "UnitPrice": 123,
                        "Quantity": 1,
                        "HostHedge": "Off",
                        "NonSensicalHedge": "Off",
                        "ObscenitiesHedge": "Off",
                        "PhoneHedge": "Off",
                        "TimeHedge": "Normal",
                        "VelocityHedge": "High",
                        "GiftCategory": "Undefined",
                        "Passenger": {
                            "Name": "Comprador accept",
                            "Identity": "1234567890",
                            "Status": "Accepted",
                            "Rating": "Adult",
                            "Email": "compradorteste@live.com",
                            "Phone": "999994444"
                        }
                    }
                ]
            },
            "Travel": {
                "Route": "MAO-RJO",
                "DepartureTime": "2010-01-02T00:00:00",
                "JourneyType": "Ida",
                "Legs": [
                    {
                        "Destination": "GYN",
                        "Origin": "VCP"
                    }
                ]
            },
            "Browser": {
                "HostName": "Teste",
                "CookiesAccepted": false,
                "Email": "compradorteste@live.com",
                "Type": "Chrome",
                "IpAddress": "200.190.150.350"
            },
            "Shipping": {
                "Addressee": "Sr Comprador Teste",
                "Phone": "21114740",
                "Method": "LowCost"
            },
            "Id": "0e4d0a3c-e424-4fa5-a573-4eabbd44da42",
            "Status": 1,
            "ReplyData": {
                "AddressInfoCode": "COR-BA^MM-BIN",
                "FactorCode": "B^D^R^Z",
                "Score": 42,
                "BinCountry": "us",
                "CardIssuer": "FIA CARD SERVICES, N.A.",
                "CardScheme": "VisaCredit",
                "HostSeverity": 1,
                "InternetInfoCode": "FREE-EM^RISK-EM",
                "IpRoutingMethod": "Undefined",
                "ScoreModelUsed": "default_lac",
                "CasePriority": 3
            }
        },
        "PaymentId": "04096cfb-3f0a-4ece-946c-3b7dc5d38f19",
        "Type": "CreditCard",
        "Amount": 100,
        "Currency": "BRL",
        "Country": "BRA",
        "ExtraDataCollection": [],
        "Status": 1,
        "ReturnCode": "4",
        "ReturnMessage": "Transação autorizada",
        "Links": [
            {
                "Method": "GET",
                "Rel": "self",
                "Href": "https://apiquerysandbox.cieloecommerce.cielo.com.br/1/sales/{PaymentId}"
            },
            {
                "Method": "PUT",
                "Rel": "capture",
                "Href": "https://apisandbox.cieloecommerce.cielo.com.br/1/sales/{PaymentId}/capture"
            },
            {
                "Method": "PUT",
                "Rel": "void",
                "Href": "https://apisandbox.cieloecommerce.cielo.com.br/1/sales/{PaymentId}/void"
            }
        ]
    }
}
"""

#variaveis de teste
MerchantID = '67e4aae9-319b-47e3-b82f-6f9661e46c71'
MerchantKey = 'TWRPQPRMWEECCFRQMHSPBIDOTWKLDRNRJKAPPRMT'
fraud_analysis = False

order = '123'

holder = 'Fulano de Tal'
e_mail = 'teste@gmail.com'
birthdate = '1991-01-02'

address_street = 'Fernando Machado'
address_number = '123-E'
address_complement = 'Centro'
address_zipCode = '89800000'
address_city = 'Chapeco'
address_state = 'SC'
address_country = 'BRA'

ccv = '123'
brand = 'Visa'
card_number = '0000000000000001'
expire_month = '12'
expire_year = '2018'
# valor em centavos
amount = 15700
installments = 5

sequence = "AuthorizeFirst"
sequence_criteria = "OnSuccess"
finger_print_id = "074c1ee676ed4998ab66491013c565e2"
cookies_accepted = False
email = "compradorteste@live.com"
host_name = "Teste"
ip_address = "200.190.150.350"
type_browser = "Chrome"
is_gift = False
returns_accepted = True

#item1
gift_category1 = "Undefined"
host_hedge1 = "Off"
non_sensical_hedge1 = "Off"
obscenities_hedge1 = "Off"
phone_hedge1 = "Off"
name1 = "ItemTeste"
quantity1 = 1,
sku1 = "201411170235134521346"
unit_price1 = 123
risk1 = "High"
time_hedge1 = "Normal"
type1 = "AdultContent"
velocity_hedge1 = "High"
email_passenger1 = "compradorteste@live.com"
identity_passenger1 = "1234567890"
name_passenger1 = "Comprador accept"
rating_passenger1 = "Adult"
phone_passenger1 = "999994444"
status_passenger1 = "Accepted"

#item2
gift_category2 = "Medical"
host_hedge2 = "Off"
non_sensical_hedge2 = "Off"
obscenities_hedge2 = "Off"
phone_hedge2 = "Off"
name2 = "ItemTeste2"
quantity2 = 10
sku2 = "2029"
unit_price2 = 10.9
risk2 = "High"
time_hedge2 = "Normal"
type2 = "AdultContent"
velocity_hedge2 = "High"
email_passenger2 = "compradorteste2@live.com"
identity_passenger2 = "09876544327"
name_passenger2 = "Comprador accept"
rating_passenger2 = "Adult"
phone_passenger2 = "999995555"
status_passenger2 = "Gold"

id1 = 95
value1 = "Eu defini isso"
id2 = 100
value2 = "E isso"

addressee = "Sr Comprador Teste"
method = "LowCost"
phone =  "21114740"

departure_time = "2010-01-02"
journey_type  = "Ida"
route = "MAO-RJO"

destination1 = "GYN"
origin1 = "VCP"
destination2 = "ABC"
origin2 = "DEF"

def create_token_card():
    # Configure o ambiente
    environment = Environment(sandbox=True)

    # Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
    merchant = Merchant(MerchantID, MerchantKey)

    # Crie uma instância de Credit Card utilizando os dados de teste
    # esses dados estão disponíveis no manual de integração
    credit_card = fills_card()

    # Cria instância do controlador do ecommerce
    cielo_ecommerce = CieloEcommerce(merchant, environment)

    # Criar a venda e imprime o retorno
    response_create_card_token = cielo_ecommerce.create_card_token(credit_card)
    print '----------------------response_create_card_token----------------------'
    print json.dumps(response_create_card_token, indent=2)
    print '----------------------response_create_card_token----------------------'

    # Com o cartão gerado token na Cielo, já temos o Token do cartão para uma futura cobrança
    new_card_token = credit_card.card_token
    return new_card_token

def authorizate_payment(token,ccv,brand,fraud_analysis):
    # Configure o ambiente
    environment = Environment(sandbox=True)

    # Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
    merchant = Merchant(MerchantID, MerchantKey)

    # Crie uma instância de Sale informando o ID do pagamento
    sale = fills_sale(token,ccv,brand)
    if fraud_analysis:
        fills_fraud_analysis(sale)

    # Cria instância do controlador do ecommerce
    cielo_ecommerce = CieloEcommerce(merchant, environment)

    # Criar a venda e imprime o retorno
    response_create_sale = cielo_ecommerce.create_sale(sale)

    print '----------------------response_create_sale----------------------'
    print json.dumps(response_create_sale, indent=2)
    print '----------------------response_create_sale----------------------'

    # Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
    # dados retornados pela Cielo
    return sale.payment

def capture_payment(payment):
    # Com o ID do pagamento, podemos fazer sua captura,
    # se ela não tiver sido capturada ainda
    # Configure o ambiente
    environment = Environment(sandbox=True)
    merchant = Merchant(MerchantID, MerchantKey)
    cielo_ecommerce = CieloEcommerce(merchant, environment)
    response_capture_sale = cielo_ecommerce.capture_sale(payment.payment_id,payment.amount, 0)
    payment.update(response_capture_sale)
    print '----------------------response_capture_sale----------------------'
    print json.dumps(response_capture_sale, indent=2)
    print '----------------------response_capture_sale----------------------'

def cancel_payment(payment):
    # E também podemos fazer seu cancelamento, se for o caso
    environment = Environment(sandbox=True)
    merchant = Merchant(MerchantID, MerchantKey)
    cielo_ecommerce = CieloEcommerce(merchant, environment)
    response_cancel_sale = cielo_ecommerce.cancel_sale(payment.payment_id, payment.amount)
    print '---------------------response_cancel_sale---------------------'
    print json.dumps(response_cancel_sale, indent=2)
    print '---------------------response_cancel_sale---------------------'

def fills_card():
    credit_card = CreditCard(ccv, brand)
    credit_card.expiration_date = expire_month + '/' + expire_year
    credit_card.card_number = card_number
    credit_card.holder = holder
    credit_card.customer_name = holder
    return credit_card

def fills_sale(token,ccv,brand):
    sale = Sale(order)

    # Crie uma instância de Customer informando o nome do cliente
    sale.customer = Customer(holder)
    sale.customer.email = e_mail
    sale.customer.birth_date = birthdate

    # cria o endereço de entrega do cliente
    sale.customer.delivery_address = Address()
    sale.customer.delivery_address.street = address_street
    sale.customer.delivery_address.city = address_city
    sale.customer.delivery_address.complement = address_complement
    sale.customer.delivery_address.country = address_country
    sale.customer.delivery_address.state = address_state
    sale.customer.delivery_address.zipCode = address_zipCode
    sale.customer.delivery_address.number = address_number

    # Cria o endereço do cliente
    sale.customer.address = Address()
    sale.customer.address.street = address_street
    sale.customer.address.city = address_city
    sale.customer.address.complement = address_complement
    sale.customer.address.country = address_country
    sale.customer.address.state = address_state
    sale.customer.address.zipCode = address_zipCode
    sale.customer.address.number = address_number

    # Crie uma instância de Credit Card utilizando os dados de teste via token
    credit_card_token = CreditCard(ccv, brand)
    credit_card_token.card_token = token

    # Crie uma instância de Payment informando o valor do pagamento
    sale.payment = Payment(amount,installments)
    sale.payment.credit_card = credit_card_token
    return sale

def fills_fraud_analysis(sale):
    sale.payment.fraud_analysis = FraudAnalysis()
    sale.payment.fraud_analysis.sequence = sequence
    sale.payment.fraud_analysis.sequence_criteria = sequence_criteria
    sale.payment.fraud_analysis.finger_print_id = finger_print_id
    sale.payment.fraud_analysis.browser = Browser()
    sale.payment.fraud_analysis.browser.host_name = host_name
    sale.payment.fraud_analysis.browser.email = email
    sale.payment.fraud_analysis.browser.cookies_accepted = cookies_accepted
    sale.payment.fraud_analysis.browser.ip_address = ip_address
    sale.payment.fraud_analysis.browser.type = type_browser
    #
    item1 = Items()
    item1.gift_category = gift_category1
    item1.host_hedge = host_hedge1
    item1.non_sensical_hedge = non_sensical_hedge1
    item1.obscenities_hedge = obscenities_hedge1
    item1.phone_hedge = phone_hedge1
    item1.name = name1
    item1.quantity = quantity1
    item1.sku = sku1
    item1.unit_price = unit_price1
    item1.risk = risk1
    item1.time_hedge = time_hedge1
    item1.type = type1
    item1.velocity_hedge = velocity_hedge1
    item1.passenger = Passenger()
    item1.passenger.email = email_passenger1
    item1.passenger.identity = identity_passenger1
    item1.passenger.name = name_passenger1
    item1.passenger.rating = rating_passenger1
    item1.passenger.phone = phone_passenger1
    item1.passenger.status_passenger = status_passenger1
    #
    # item2 = Items()
    # item2.gift_category = gift_category2
    # item2.host_hedge = host_hedge2
    # item2.non_sensical_hedge = non_sensical_hedge2
    # item2.obscenities_hedge = obscenities_hedge2
    # item2.phone_hedge = phone_hedge2
    # item2.name = name2
    # item2.quantity = quantity2
    # item2.sku = sku2
    # item2.unit_price = unit_price2
    # item2.risk = risk2
    # item2.time_hedge = time_hedge2
    # item2.type = type2
    # item2.velocity_hedge = velocity_hedge2
    # item2.passenger = Passenger()
    # item2.passenger.email = email_passenger2
    # item2.passenger.identity = identity_passenger2
    # item2.passenger.name = name_passenger2
    # item2.passenger.rating = rating_passenger2
    # item2.passenger.phone = phone_passenger2
    # item2.passenger.status_passenger = status_passenger2
    #
    sale.payment.fraud_analysis.item = [item1]#, item2]

    merchant_defined_filds1 = MerchantDefinedFields()
    merchant_defined_filds1.id = id1
    merchant_defined_filds1.value = value1
    #
    # merchant_defined_filds2 = MerchantDefinedFields()
    # merchant_defined_filds2.id = id2
    # merchant_defined_filds2.value = value2
    #
    sale.payment.fraud_analysis.merchant_definid_fields = [merchant_defined_filds1]#,merchant_defined_filds2]

    sale.payment.fraud_analysis.shipping = Shipping()
    sale.payment.fraud_analysis.shipping.addressee = addressee
    sale.payment.fraud_analysis.shipping.method = method
    sale.payment.fraud_analysis.shipping.phone = phone

    sale.payment.fraud_analysis.travel = Travel()
    sale.payment.fraud_analysis.travel.departure_time = departure_time
    sale.payment.fraud_analysis.travel.journey_type = journey_type
    sale.payment.fraud_analysis.travel.route = route

    legs1 = Legs()
    legs1.destination = destination1
    legs1.origin = origin1
    #
    # legs2 = Legs()
    # legs2.destination = destination2
    # legs2.origin = origin2
    #
    sale.payment.fraud_analysis.travel.legs = [legs1]#, legs2]

    return sale

token = create_token_card()
payment = authorizate_payment(token, ccv, brand, fraud_analysis)
if payment.return_message == "Operation Successful":
    capture_payment(payment)
    cancel_payment(payment)
elif payment.return_message == "Not Authorized":
    print "Transação não autorizada, tente com outro cartão"
elif payment.return_message == "Card Expired":
    print "Cartão Expirado, tente com outro"
elif payment.return_message == "Blocked Card":
    print "Cartão Bloqueado, tente com outro"
elif payment.return_message == "Timed Out":
    print "Tempo de conexão excedido, tente novamente"
elif payment.return_message == "Card Canceled":
    print "Cartão Cancelado, tente com outro"
elif payment.return_message == "Problems with Creditcard":
    print "Problemas com o seu cartão de Crédito, tente com outro"
else:
    print "Erro com o Retorno da Integração"
```

## Manual Oficial da Cielo

Para mais informações sobre a integração com a API 3.0 da Cielo, vide o manual em: [Integração API 3.0](https://developercielo.github.io/Webservice-3.0/)
