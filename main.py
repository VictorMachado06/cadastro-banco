usuario = input('Digite seu nome: ')
saldo = 0
print(f'\nOlá {usuario}, O que você deseja fazer hoje?')
opcao = ''
while opcao != '4':
    print('''\n[1] - Consultar saldo
[2] - Depositar
[3] - Sacar
[4] - Sair''')
    opcao = input('Escolha uma opção: ').strip()
    while opcao not in ('1', '2', '3', '4'):
        print('Opção invalida!')
        opcao = input('Escolha uma opção: ').strip()
    if opcao == '1':
        print(f'Seu saldo é R$ {saldo:.2f}')
    elif opcao == '2':
        deposito = float(input('Digite o valor do deposito: R$ '))
        if deposito > 0:
            saldo += deposito
            print('Depósito realizado com sucesso!')
            print(f'Saldo Atual: R$ {saldo:.2f}')
        else:
            print('O valor de depósito deve ser positivo!')
    elif opcao == '3':
        saque = float(input('Digite o valor do saque: R$ '))
        if saque <= 0:
            print('O valor do saque deve ser positivo!')
        elif saque > saldo:
            print('Saldo insuficiente para saque!')
        else:
            saldo -= saque
            print('Saque realizado com sucesso!')
            print(f'Saldo Atual: R$ {saldo:.2f}')
print(f'Até mais, {usuario}')
