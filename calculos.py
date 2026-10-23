from storage import *

def calcular_imc(peso , altura):
    imc = peso / (altura * 2)
    return imc

def clas_imc(imc):
    resultado = ''
    if imc < 18.5:
        resultado = 'Abaixo do peso'
        return resultado
    elif imc >= 18.5 and imc < 24.9:
        resultado = 'Peso Normal'
        return resultado
    elif imc >= 25 and imc < 29.9:
        resultado = 'Sobrepeso'
        return resultado
    elif imc >= 30 and imc < 34.9:
        resultado = 'Obesidade Grau I'
        return resultado
    elif imc >= 35 and imc < 39.9:
        resultado = 'Obesidade Grau II'
        return resultado
    else :
        resultado = 'Obesidade Grau III'
        return resultado

pessoa = co_dados()
imc = calcular_imc()