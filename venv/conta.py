class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
        print('Deposito de {} - Novo saldo de {} do titular {}'.format(valor, self.__saldo, self.__titular))

    def saca(self, valor):
        self.__saldo -= valor
        print('Saque de {} - Novo saldo de {} do titular {}'.format(valor, self.__saldo, self.__titular))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print('Transferência de {} realizada com sucesso da conta {} para a conta {}'.format (valor, origem, destino))
