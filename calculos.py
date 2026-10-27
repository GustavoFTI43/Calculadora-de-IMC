from storage import *



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

def calcular_imc():
    arquivo = carregar_arquivo()
    dados = co_dados()
    while True:
        try:
            imc = dados["peso"] / (dados["altura"] ** 2)
            dados["IMC"] = round (imc , 2)
            dados['classificação'] = clas_imc(imc)
        except ZeroDivisionError:
            print('Preencha os dados corretamente pois não é possivel realizar divisão por zero')
            break
        except TypeError:
            print('Preencha todos os dados para poder continuar .')
            break
        else :
            arquivo.append(dados)
            salvar_arquivo(arquivo)
            return f'IMC: {imc: .2f} - {dados["classificação"]}'