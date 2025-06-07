'''#Exercício 1
dicionarioBrasil = {'Amazonas': 'Manaus',
                    'Bahia': 'Salvador',
                    'Brasília': 'Goiânia',
                    'Rio de Janeiro': 'Rio de Janeiro',
                    'Paraná': 'Curitiba'}
for estado, capital in dicionarioBrasil.items():
    print('A capital de', estado, 'é', capital)'''

'''#Exercício 2
dicionarioAlunos = {'Emilyn': [60, 70, 80],
                    'Komadaki': [65, 75, 85],
                    'Sakai': [70, 80, 90]}
    for aluno, nota in dicionarioAlunos.items():
    media = sum(nota) / len(nota)
    if media >= 60:
        mensagem = ('aprovado')
    else:
        mensagem = ('reprovado')
    print(aluno, 'possui a média', media, 'e foi', mensagem)'''

'''#Exercício 3
setFrutas = {'Morango', 'Manga', 'Abacaxi'}

setNovasFrutas = setFrutas.copy()
setNovasFrutas.add('Uva')

print('O conjunto de frutas original era', setFrutas, ', agora o novo conjunto de frutas é', setNovasFrutas)'''

'''#Exercício 4
participantes = ['Maria', 'José', 'joão', 'Maria']
setSemRepeticoes = set(participantes)
quantidadePartipantes = len(setSemRepeticoes)
participantesUnicos = [setSemRepeticoes]

print('Os participantes sem repetições são', participantesUnicos, 'no qual existem', quantidadePartipantes, 'participantes')'''

'''#Exercício 5
from math import sqrt as raiz 
print(raiz(625))

#Bom dia, shimano!!!!
#Bom dia, shimano!!!!
#Bom dia, shimano!!!!
#Bom dia, shimano!!!!
#Bom dia, shimano!!!!
'''

#Exercício 6
from calculos import dobro_mais_raiz
print(dobro_mais_raiz(16))
