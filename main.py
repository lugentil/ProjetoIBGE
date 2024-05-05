import pandas as pd
df = pd.read_excel('C:\\Users\\Lucas\\Desktop\\Projeto-IBGE\\Municipios.xls').sample(n=100)
df.columns = ['Cidade', 'Território', 'População']

def programa():
    menu()
    for i in range(1,10):
        try:
            resposta = int(input())
            break
        except:
            print(f'O valor informado é ínválido.\nPor favor escolher entre as opções válidas.')

    while (resposta != 0):
        modulos(resposta)

    if ( resposta == 0):
        print(f'Obrigado por utilizar o programa, até breve!')
        exit()

def menu():
    print(f'Bem vindo ao programa de consulta de dados IBGE da região de SP!')
    print(f'-----------------------------------------------')
    print(f'1 - Cidade mais extensa')
    print(f'2 - Cidade mais populosa')
    print(f'3 - Média de pópulação do estado de SP')
    print(f'4 - Busca por Cidade')
    print(f'0 - Para sair do Programa')

def calcula_territorio_mais_extenso():
    ID = df['Território'].idxmax()
    Cidade = df.loc[ID,'Cidade']
    Territorio = df.loc[ID,'Território']
    print(f'{Cidade} possui o maior território entre todas as cidades do Estado de São Paulo com {Territorio} km².')
    return

def calcula_populacao_mais_extenso():
    ID = df['Território'].idxmax()
    Cidade = df.loc[ID,'Cidade']
    População = df.loc[ID,'População']
    print(f'{Cidade} possui a maior população entre todas as cidades do Estado de São Paulo com {População} habitantes.')

def calcula_media_populacao_estado():
    População = df['População'].sum()
    Media = População / len(df)
    print(f'Média da População entre as 100 cidades é equivalente a {round(Media)} pessoas.')

def buscar():
    print(f'\nOpções de busca:')
    print(f'\n1 - População > x')
    print(f'\n2 - População < x')
    print(f'\n3 - Território > x')
    print(f'\n4 - Território < x')
    print(f'\n5 - Nome')
    for i in range(1,10):
        try:
            busca = int(input())
            break
        except:
            print(f'O valor informado é ínválido.\nPor favor escolher entre as opções válidas.')
    if busca == 1:
        print(f'Por gentileza fornecer um número inteiro para buscar no dataset.')
        x = int(input())
        cidade_busca = df[df['População'] > x]['Cidade']
        população_busca = df[df['População'] > x]['População']
        territorio_busca = df[df['Território'] > x]['População']

        print(f'Realizando busca...\nResultados:\n')
        for i, j, k in zip(cidade_busca, população_busca, territorio_busca):
            print(f'{i} Habitantes: {j} Território: {k} km²')
            print('\n|------------------------------------------------------------------------------------------------------|\n')
    elif busca == 2:
        print(f'Por gentileza fornecer um número inteiro para buscar no dataset.')
        x = int(input())
        cidade_busca = df[df['População'] < x]['Cidade']
        população_busca = df[df['População'] < x]['População']
        territorio_busca = df[df['Território'] < x]['População']
        print(f'Realizando busca...\nResultados:\n')
        for i, j, k in zip(cidade_busca, população_busca, territorio_busca):
            print(f'{i} Habitantes: {j} Território: {k} km²')
            print('\n|------------------------------------------------------------------------------------------------------|\n')
    elif busca == 3:
        print(f'Por gentileza fornecer um número inteiro para buscar no dataset.')
        x = int(input())
        cidade_busca = df[df['Território'] > x]['Cidade']
        população_busca = df[df['Território'] > x]['População']
        territorio_busca = df[df['Território'] > x]['Território']
        print(territorio_busca)
        print(f'Realizando busca...\nResultados:\n')
        for i, j, k in zip(cidade_busca, população_busca, territorio_busca):
            print(f'{i} Habitantes: {j} Território: {k} km²')
            print('\n|------------------------------------------------------------------------------------------------------|\n')
    elif busca == 4:
        print(f'Por gentileza fornecer um número inteiro para buscar no dataset.')
        x = int(input())
        cidade_busca = df[df['Território'] < x]['Cidade']
        população_busca = df[df['Território'] < x]['População']
        territorio_busca = df[df['Território'] < x]['Território']
        print(f'Realizando busca...\nResultados:\n')
        for i, j, k in zip(cidade_busca, população_busca, territorio_busca):
            print(f'Cidade: {i} Habitantes: {j} Território: {k} km²')
            print('\n|------------------------------------------------------------------------------------------------------|\n')
    elif busca == 5:
        print(f'Por gentileza fornecer o nome da cidade para buscar no dataset.')
        nome = input()
    elif busca == 0:
        return


def modulos(resposta):
    if int(resposta) == 1:
        calcula_territorio_mais_extenso()
        print(f'\nPara voltar ao menu pressione "0"')
        if int(input()) == 0:
            return programa()
    elif int(resposta) == 2:
        calcula_populacao_mais_extenso()
        print(f'\nPara voltar ao menu pressione "0"')
        if int(input()) == 0:
            return programa()
    elif int(resposta) == 3:
        calcula_media_populacao_estado()
        print(f'\nPara voltar ao menu pressione "0"')
        if int(input()) == 0:
            return programa()
    elif int(resposta) == 4:
        buscar()
        print(f'\nPara voltar ao menu pressione "0"')
        if int(input()) == 0:
            return programa()
    else:
        for i in range(1,100):
            print()
        print(f'Por gentileza informar 1 número válido.')
        print(f'\nOpções:')
        print(f'1 - Cidade mais extensa')
        print(f'2 - Cidade mais populosa')
        print(f'3 - Média de pópulação do estado de SP')
        print(f'4 - Busca por Cidade')
        print(f'0 - Para sair do Programa')
        resposta = int(input())
        if resposta == 0:
            print(f'Obrigado por utilizar o programa, até breve!')
            exit()

        return modulos(resposta)



if __name__ == '__main__':
    programa()
