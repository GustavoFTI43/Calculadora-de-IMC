from storage import *
from time import sleep
from calculos import *


while True:
    menu(['Calcular IMC' , 'Ver Historio' , 'Sair'])
    resp = selctoption()

    if resp == 1:
        result = calcular_imc()
        if result is None:
            sleep(1)
            continue
        else:
            print(f'{result}\n Dado Salvo em Registros !')
            sleep(2)
    elif resp == 2:
        historico()
        sleep(2)
    else :
        print('Encerrando ....')
        sleep(1)
        print('                 Até logo ...')
        break