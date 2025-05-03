print("Hello, World!")

#exercício1
nome = 'Lily'
idade = 32
cpf = '123.456.789-00'
print("Meu nome é", nome, "e tenho", idade, "anos. Meu CPF é", cpf)



#exercício2
data = input("Qual a data de hoje? ")
print("Hoje é dia", data)
nome_usuario = input("Insira o seu nome: ")
idade_usuario = input("Agora insira a sua idade: ")
comida_favorita = input("Qual a sua comida favorita? ")
print("Seu nome é", nome_usuario) # Dá pra usar a tag /n para dar quebra de linha, aí não precisaria printar 3x.
print("Sua idade é", idade_usuario,"anos") # A tag /t serve pra dar um tab.
print("Sua comida favorita é", comida_favorita)



#exercicio3
a = 2
b = 7
soma = (a + b)
print("A soma de 2 e 7 é igual a", soma)

c = 45
divisao = c / 2
print("A divisão de 45 pela metade é igual a", divisao)

d = 9
potencia_quadrada = d ** 2
print("O número 9 elevado ao quadrado é igual a", potencia_quadrada)

e = 14
resto_divisao = e % 3
print("O resto da divisão de 14 por 3 é", resto_divisao)



#exercício4
ano_nascimento_usuario = int(input("Insira o ano do seu nascimento: "))
ano_atual = int(input("Insira em qual ano estamos: "))
idade_do_usuario = ano_atual - ano_nascimento_usuario
print("Você tem", idade_do_usuario, "anos")

valor_reais = float(input("Insira um valor em reais: "))
valor_dolar = 5
conversao_real_dolar = valor_reais / valor_dolar
print("O seu valor de reais em dólar é igual a", conversao_real_dolar, "dólares")

A = int(input("Insira o valor de A: "))
B = int(input("Insira o valor de B: "))
C = int(input("Insira o valor de C: "))
calculo_delta = (B ** 2) - (4 * A * C)
calculo_bhaskara_x1 = (-B + (calculo_delta ** (1/2))) / (2 * A)
calculo_bhaskara_x2 = (-B - (calculo_delta ** (1/2))) / (2 * A)
print("O valor de x1 é igual a", calculo_bhaskara_x1, "e o valor do seu x2 é igual a", calculo_bhaskara_x2)



#exercício5
idade = int(input("Insira a sua idade: "))
if(idade < 18):
    print("Você é menor de idade.")
elif(idade < 60):
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

nota1 = float(input("Insira a sua nota 1: "))
nota2 = float(input("Insira a sua nota 2: "))
nota3 = float(input("Insira a sua nota 3: "))
media_nota = (nota1 + nota2 + nota3) / 3
if(media_nota >= 60):
    print("Aprovado!:)")
else:
    print("Exame!:(") 