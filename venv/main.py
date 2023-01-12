from conta import Conta

conta = Conta(123, 'Fabiano', 55.5, 1000.0)
conta2 = Conta(321, 'Marco', 100.0, 1000.0)

conta.extrato()
conta2.extrato()

print('*'*10)

conta.deposita(10)
conta2.deposita(10)

print('*'*10)

conta.saca(30)
conta2.saca(20)