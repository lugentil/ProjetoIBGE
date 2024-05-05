import pandas as pd

def programa():
    df = pd.read_excel('C:\\Users\\Lucas\\Desktop\\Projeto-IBGE\\Municipios.xls')
    print(df)
    menu()
    resposta = int(input())
    while (resposta != 0):
        modulos(resposta)

    if ( resposta == 0):
        print(f'Obrigado por utilizar o programa, até breve!')

def menu():
    print(f'Bem vindo ao programa de consulta de dados IBGE da região de SP!')
    print(f'-----------------------------------------------')
    print(f'1 - Cidade mais extensa')
    print(f'2 - Cidade mais populosa')
    print(f'2 - Cidade mais populosa')
    print(f'3 - Média de pópulação do estado de SP')
    print(f'4 - Média de pópulação do estado de SP')
    print(f'5 - Busca por Cidade')
    print(f'0 - Para sair do Programa')

def calcula_mais_extensa():
    testes = print(f'Funcionando')
    return testes

def modulos(resposta):
    if int(resposta) == 1:
        calcula_mais_extensa()
        print(f'Para voltar ao menu pressione "0"')
        if int(input()) == 0:
            return programa()


if __name__ == '__main__':
    programa()
