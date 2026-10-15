usuario = input('Digite seu nome: ')
saldo = 0
historico = []
print(f'\nOlá {usuario}, O que você deseja fazer hoje?')
opcao = ''
while opcao != '5':
    print('''\n[1] - Consultar saldo
[2] - Depositar
[3] - Sacar
[4] - Ver histórico
[5] - Sair''')
    opcao = input('Escolha uma opção: ').strip()
    while opcao not in ('1', '2', '3', '4', '5'):
        print('\nOpção invalida!')
        opcao = input('Escolha uma opção: ').strip()
    if opcao == '1':
        print(f'\nSeu saldo é R$ {saldo:.2f}')
    elif opcao == '2':
        deposito = float(input('\nDigite o valor do deposito: R$ '))
        if deposito > 0:
            saldo += deposito
            historico.append(f'Depósito: R$ {deposito:.2f}')
            print('Depósito realizado com sucesso!')
            print(f'Saldo Atual: R$ {saldo:.2f}')
        else:
            print('O valor de depósito deve ser positivo!')
    elif opcao == '3':
        saque = float(input('\nDigite o valor do saque: R$ '))
        if saque <= 0:
            print('O valor do saque deve ser positivo!')
        elif saque > saldo:
            print('Saldo insuficiente para saque!')
        else:
            saldo -= saque
            historico.append(f'Saque: R$ {saque:.2f}')
            print('Saque realizado com sucesso!')
            print(f'Saldo Atual: R$ {saldo:.2f}')
    elif opcao == '4':
        print('\nHistórico de transações:')
        if len(historico) == 0:
            print('Nenhuma movimentação realizada.')
        else:    
            for movimentacao in historico:
                print(movimentacao)

print(f'\nAté mais, {usuario}')
