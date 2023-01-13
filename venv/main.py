from conta import Conta

conta = Conta(123, 'Fabiano', 55.5, 1000.0)
conta2 = Conta(321, 'Marco', 100.0, 1000.0)


conta.saca(100)


codigos = Conta.codigos_bancos()

print(codigos['BB'])