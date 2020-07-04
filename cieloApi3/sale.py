
from .objectJSON import ObjectJSON

class Sale(ObjectJSON):

    def __init__(self, merchant_order_id):

        # Order
        self.merchant_order_id = merchant_order_id

        # Dados do Comprador
        self.customer = None

        # Dados do Pagamento
        self.payment = None

    def update_return(self, r):

        payment = r.get('Payment') or {}
        if payment.get('PaymentId'):
            self.payment.payment_id = payment.get('PaymentId')
        if payment.get('Url'):
            self.payment.url = payment.get('Url')
        if payment.get('ReturnMessage'):
            self.payment.return_message = payment.get('ReturnMessage')
        if payment.get('ProofOfSale'):
            self.payment.proof_of_sale = payment.get('ProofOfSale')
        if payment.get('Tid'):
            self.payment.tid = payment.get('Tid')
        if payment.get('AuthorizationCode'):
            self.payment.authorization_code = payment.get('AuthorizationCode')
        if payment.get('SoftDescriptor'):
            self.payment.soft_descriptor = payment.get('SoftDescriptor')

        if self.payment.recurrent_payment:
            recurrent = payment.get('RecurrentPayment') or {}
            self.payment.recurrent_payment.recurrent_payment_id = recurrent.get('RecurrentPaymentId')

        if self.payment.fraud_analysis:
            fraud_analysis = payment.get('FraudAnalysis') or {}
            if fraud_analysis.get('Status'):
                self.payment.fraud_analysis.status = fraud_analysis.get('Status')
            if fraud_analysis.get('Id'):
                self.payment.fraud_analysis.id = fraud_analysis.get('Id')
            if fraud_analysis.get('IsRetryTransaction'):
                self.payment.fraud_analysis.is_retry_transaction = fraud_analysis.get('IsRetryTransaction')
            if fraud_analysis.get('TotalOrderAmount'):
                self.payment.fraud_analysis.total_order_amount = fraud_analysis.get('TotalOrderAmount')

            reply_data = fraud_analysis.get('ReplyData') or {}

            if reply_data.get('AddressInfoCode'):
                self.payment.fraud_analysis.reply_data.address_info_code = reply_data.get('AddressInfoCode')
            if reply_data.get('FactorCode'):
                self.payment.fraud_analysis.reply_data.factor_code = reply_data.get('FactorCode')
            if reply_data.get('Score'):
                self.payment.fraud_analysis.reply_data.score = reply_data.get('Score')
            if reply_data.get('BinCountry'):
                self.payment.fraud_analysis.reply_data.bin_country = reply_data.get('BinCountry')
            if reply_data.get('CardIssuer'):
                self.payment.fraud_analysis.reply_data.card_issuer = reply_data.get('CardIssuer')
            if reply_data.get('CardScheme'):
                self.payment.fraud_analysis.reply_data.card_scheme = reply_data.get('CardScheme')
            if reply_data.get('HostSeverity'):
                self.payment.fraud_analysis.reply_data.host_severity = reply_data.get('HostSeverity')
            if reply_data.get('InternetInfoCode'):
                self.payment.fraud_analysis.reply_data.internet_info_code = reply_data.get('InternetInfoCode')
            if reply_data.get('IpRoutingMethod'):
                self.payment.fraud_analysis.reply_data.ip_routing_method = reply_data.get('IpRoutingMethod')
            if reply_data.get('ScoreModelUsed'):
                self.payment.fraud_analysis.reply_data.score_model_used = reply_data.get('ScoreModelUsed')
            if reply_data.get('CasePriority'):
                self.payment.fraud_analysis.reply_data.case_priority = reply_data.get('CasePriority')
