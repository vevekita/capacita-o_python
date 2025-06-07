def dobro_mais_raiz(numero: float) -> float:
    dobroRaiz = (numero * 2) + (numero ** (1/2))
    return dobroRaiz
print(dobro_mais_raiz(16))