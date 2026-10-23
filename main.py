from storage import *
from time import sleep


while True:
    menu(['Calcular IMC' , 'Ver Historio' , 'Sair'])
    resp = selctoption()

    if resp == 1:
        print('Calcular')
        sleep(2)
    elif resp == 2:
        print('Historico')
        sleep(2)
    else :
        print('Encerrando ....')
        sleep(1)
        print('                 Até logo ...')
        break