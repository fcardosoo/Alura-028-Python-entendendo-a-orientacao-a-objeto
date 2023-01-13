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
        print('Deposito de R${} | Novo saldo de R${} do titular {}'.format(valor, self.__saldo, self.__titular))

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
            print('Saque de R${} | Novo saldo de R${} do titular {}'.format(valor, self.__saldo, self.__titular))
        else:
            print('Você não posssui saldo suficiente para esta operação! Valor disponível para saque é R${}'.format(self.__saldo+self.__limite))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print('Transferência de R${} realizada com sucesso da conta {} para a conta {}'.format (valor, self.__numero, destino))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite