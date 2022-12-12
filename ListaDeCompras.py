import os


def risk():
    print('-=' * 9)


lista = []


def title():
    print('Lista de Compras!')


def optionI():
    items = input('Digite um item para inserir: ')
    lista.append(items)


def optionA():
    deletStr = input('Qual item você deseja excluir: ')
    try:
        delete = int(deletStr)
        del lista[delete]
    except IndexError:
        print('Índice não existe na lista!')
    except TypeError:
        print('Por favor digite um número inteiro!')
    except Exception:
        print('Erro desconhecido!')


def optionL():
    if len(lista) == 0:
        print('Não a nada para mostrar!')
    for indice, nome in enumerate(lista):
        print(indice, nome)


risk()
title()
risk()

while True:
    print('Digite uma das opções:')
    option = input('[i]nserir [a]pagar [l]istar: ')

    if option == 'i':
        os.system('cls')
        optionI()
    elif option == 'a':
        optionA()
    elif option == 'l':
        os.system('cls')
        optionL()
