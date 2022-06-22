"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    altura_max = 0
    altura_min = 10000000
    nome_altura_max = ''
    nome_altura_min = ''
    peso_max = 0
    peso_min = 10000
    nome_peso_max = ''
    nome_peso_min = ''
    media_altura = 0
    media_peso = 0
    total_altura = 0
    total_peso = 0
    pessoas = {}

    try:

        while True:
            # transformar a entrada em um dicionário e usar reduce para calcular a média
            # e tentar usar map e filter
            nome = input('Nome: ')
            altura = float(input('Altura: '))
            peso = float(input('Peso: '))
            pessoas[nome] = {'altura': altura, 'peso': peso}
            if nome == '0':
                break
            if altura > altura_max:
                altura_max = altura
                nome_altura_max = nome
            if altura < altura_min:
                altura_min = altura
                nome_altura_min = nome
            if peso > peso_max:
                peso_max = peso
                nome_peso_max = nome
            if peso < peso_min:
                peso_min = peso
                nome_peso_min = nome
            total_altura += altura
            total_peso += peso

    except:
        print(f'Cliente mais alto: {nome_altura_max}, com {altura_max:.0f} centímetros')
        print(f'Cliente mais baixo: {nome_altura_min}, com {altura_min:.0f} centímetros')
        print(f'Cliente mais magro: {nome_peso_min}, com {peso_min:.0f} kilos')
        print(f'Cliente mais gordo: {nome_peso_max}, com {peso_max:.0f} kilos')
        print('--------------------------------------------------')
        print(f'Media de altura dos clientes: {(total_altura / len(pessoas)):.1f} centímetros')
        print(f'Media de peso dos clientes: {(total_peso / len(pessoas)):.1f} kilos')



