#Exercício 1
lista_compras = []
lista_compras.append('Arroz') #append adiciona o elemento na última posição da lista
lista_compras.append('Feijão')
lista_compras.append('Leite')
lista_compras.insert(0, 'Pão') #insert adiciona um elemento em uma posição específica da lista
print(lista_compras)
lista_compras.remove('Feijão') #remove um elemento específico
lista_compras.pop(-1) #pop remove o último elemento
print(lista_compras)

#Exercício 2
print("Por favor, digite 3 números inteiros: ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
lista_numeros = [num1, num2, num3]
soma = (lista_numeros[0] + lista_numeros[1] + lista_numeros[2])
print("A soma dos números inseridos é igual a:", soma)

#Exercício 3
lista_fruta = ['Abacaxi', 'Maçã', 'Morango', 'Mexirica', 'Abacate']
for fruta in lista_fruta:
    print(fruta)

#Exercício 4
numeros = [20, 16, 48, 23, 60]
maior = numeros[0]
print("Maior iniciando com:", maior)
for numero in numeros:
    print("Máximo atual é:", maior)
    print("Número sendo visto é:", numero)
    if numero > maior:
        maior = numero
    print()
print("O maior número da lista é:", maior)

#Exercício 5
for i in range(21):
    par = i % 2
    if par == 0:
        print(i)

#Exercício 6
lista_inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = []
impar = []
    for numeros in lista_inteiros:
        if numeros % 2 == 0:
            par.append(numeros)
        else:
            impar.append(numeros)

print("A lista de números pares é:", par)
print("A lista de números ímpares é:", impar)
        
    
