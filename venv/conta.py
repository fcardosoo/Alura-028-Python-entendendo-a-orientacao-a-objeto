class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor
        print('Deposito de {} - Novo saldo de {} do titular {}'.format(valor, self.saldo, self.titular))

    def saca(self, valor):
        self.saldo -= valor
        print('Saque de {} - Novo saldo de {} do titular {}'.format(valor, self.saldo, self.titular))