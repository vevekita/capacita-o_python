
# Exercício 1
numero = 0
while numero < 21:
    numero += 1
    if numero % 2 == 0:
        print(numero)

# Exercício 2
senha = input('Crie uma senha: ')
digite = input('Digite a senha: ')
while senha != digite:
    digite = input('Senha incorreta! Tente novamente: ')
    if senha == digite:
        print('Senha correta!')

# Exercício 3
saldo = 1000
opcao = 0
while opcao != 4:
    print('\nO que você deseja fazer?')
    print('Digite: 1 para sacar; 2 para depositar, 3 para mostrar o saldo e 4 para sair.')
    opcao = int(input('Digite o número do que deseja: '))

    if opcao == 1:
        valorSacar = int(input('Quanto você deseja sacar? '))
        if saldo - valorSacar < 0:
            print('Esse valor não pode ser sacado por ser maior do que o saldo atual.')
        else:
            saldo = saldo - valorSacar
            print('Você sacou', valorSacar)
    elif opcao == 2:
        valorDepositar = int(input('Quanto você deseja depositar? '))
        saldo = saldo + valorDepositar
        print('Você depositou', valorDepositar)
    elif opcao == 3:
        print(saldo)
    elif opcao == 4:
        print('Até a próxima!')

# Exercício 4
def saudacao_personalizada(nome: str):
    mensagem = 'bom dia ' + nome + ', como está hoje?'
    print(mensagem)

saudacao_personalizada('SHISHI')

# Exercício 5
multiplicador = 2
def multiplica(num: float):
    resultado = multiplicador * num
    print(resultado)

multiplica(3)



    