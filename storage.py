from pathlib import Path
import json
from datetime import datetime

arq_json= Path('registropessoas.json')
def carregar_arquivo():
    try:
        if not arq_json.exists():
            with open(arq_json , 'w' , encoding='utf-8') as arquivo:
                json.dump([],arquivo)

        with open(arq_json , 'r' , encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError as e:
        print(f'Json corrompido {e}')

    else:
        try:
            if arq_json.exists():
                with open(arq_json , 'r' , encoding='utf-8') as arquivo:
                    return json.load(arquivo)
        except IOError as e:
            print(f'Error ao abrir arqivo: {e}')


def salvar_arquivo(dado_novo):
    try:
        with open(arq_json, 'w' , 'utf-8') as arquivo:
            json.dump(dado_novo , arquivo , indent=4 , ensure_ascii=False)
    except IOError as e:
        print(f'Error ao abrir arqivo: {e}')
    except TypeError as e:
        print(f'Dado nâo Pode ser Convertido para Json : {e}')


def leia_float(msg):
    while True:
        try:
            v_float = float(input(msg).replace(',','.'))
            if v_float > 0:
                  return v_float
            else:
                 print(f'Digite apenas valores positivos(acima de 0) !')
                 continue   
        except ValueError:
            print(f'Erro : Digite apenas valores validos !')
            continue
        except KeyboardInterrupt:
            print(f'\nErro : Nenhum valor digitador !')
            break

def DateRef():
    YY = datetime.now().year
    MM = datetime.now().month
    DD = datetime.now().day
    return f'{DD}/{MM}/{YY}'


def co_dados():
    dados = dict()
    dados['nome'] = str(input('digite seu nome completo : ')).strip().title()
    dados['peso']= leia_float('Digite seu peso: ')
    dados['altura']= leia_float('Digite sua altura: ')
    dados['data'] = DateRef()
    return dados


def menu(lista):
    titulo('Calculadora de IMC' , 3)
    for c ,v in enumerate(lista):
        if c != 2:
            print(f'[{c + 1}] {v}')
        else:
            print(f'[{c - 2}] {v}')


def selctoption():
    while True:
        try:
            opcao = int(input('Digite Uma Das Opções Acima: '))
        except ValueError:
            print(f'Erro: digite um valor valido . Tente novamente ...')
        except KeyboardInterrupt:
            print(f'Erro: Não foi digitado nenhum valor ...')
            return 0
        else :
            if opcao not in range(0 , 3):
                print(f'Opção invalida  : Tente novamente , Escolha entre 0 a 2 como as opções acima !!!')
            else :
                return opcao



def titulo(msg , mult = 0):
    cont_carac = (len(msg) + 4) * mult
    print(f'{"-" * cont_carac}\n{msg: ^{cont_carac}}\n{"-" * cont_carac}')


def quebralinha():
    print('-' * 70)

