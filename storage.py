from pathlib import Path
import json

arq_json= Path('registropessoas.json')
def verifica_existe():
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


def co_dados():
    dados = dict()
    dados['nome'] = str(input('digite seu nome completo : ')).strip().title()
    dados['peso']= leia_float('Digite seu peso: ')
    dados['altura']= leia_float('Digite sua altura: ')
    return dados

