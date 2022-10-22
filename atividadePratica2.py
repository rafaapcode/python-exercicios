# Exibindo o Menu
print('+------------------- Bem-Vindo a Sorveteria do Rafael Aparecido Gonçalves da Silva -----------------+')
print('+ Código |       Descrição      |   Tamanho P (500ml)  | Tamanho M (1000ml) | Tamanho G (2000ml) | +')
print('+  TR    | Sabores Tradicionais |      R$ 6,00         |      R$ 10,00      |      R$ 18,00      | +')
print('+  ES    |   Sabores Especiais  |      R$ 7,00         |      R$ 12,00      |      R$ 21,00      | +')
print('+  PR    |    Sabores Premium   |      R$ 8,00         |      R$ 14,00      |      R$ 24,00      | +')
print('+--------------------------------------------------------------------------------------------------+')

# Inicialiando variável de valor
valor = 0

while True:

    # Entrada de dados do usuário
    tamanho = input('Qual tamanho de sorvete deseja ? (P , M , G) ')
    codigo = input('Digite o código do sorvete desejado: ')
    
    if codigo.upper() == 'TR' :
        
        if tamanho.upper() == 'P':
            valor += 6
            print('Você pediu um sorvete Sabor Tradicional tamanho P de R$ 6,00 ')
            print('-------------------------------------------------------------')
        elif tamanho.upper() == 'M':
            valor += 10
            print('Você pediu um sorvete Sabor Tradicional tamanho M de R$ 10,00 ')
            print('-------------------------------------------------------------')
        elif tamanho.upper() == 'G':
            valor += 18
            print('Você pediu um sorvete Sabor Tradicional tamanho G de R$ 18,00 ')
            print('-------------------------------------------------------------')
        else :
            print('!!!!!!! ---- TAMANHO ou CÓDIGO inválido(s) ---- !!!!!!!')
            print('-------------------------------------------------------------')
            continue # Volta o loop do começo
    elif codigo.upper() == 'ES' :
        
        if tamanho.upper() == 'P':
            valor += 7
            print('Você pediu um sorvete Sabor Especial tamanho P de R$ 7,00 ')
            print('-------------------------------------------------------------')
        elif tamanho.upper() == 'M':
            valor += 12
            print('Você pediu um sorvete Sabor Especial tamanho M de R$ 12,00 ')
            print('-------------------------------------------------------------')
        elif tamanho.upper() == 'G':
            valor += 21
            print('Você pediu um sorvete Sabor Especial tamanho G de R$ 21,00 ')
            print('-------------------------------------------------------------')
        else :
            print('!!!!!!! ---- TAMANHO ou CÓDIGO inválido(s) ---- !!!!!!!')
            print('-------------------------------------------------------------')
            continue # Volta o loop do começo
    elif codigo.upper() == 'PR' :
        
        if tamanho.upper() == 'P':
            valor += 8
            print('Você pediu um sorvete Sabor Premium tamanho P de R$ 8,00 ')
            print('-------------------------------------------------------------')
        elif tamanho.upper() == 'M':
            valor += 14
            print('Você pediu um sorvete Sabor Premium tamanho M de R$ 14,00 ')
            print('-------------------------------------------------------------')
        elif tamanho.upper() == 'G':
            valor += 24
            print('Você pediu um sorvete Sabor Premium tamanho G de R$ 24,00 ')
            print('-------------------------------------------------------------')
        else :
            print('!!!!!!! ---- TAMANHO ou CÓDIGO inválido(s) ---- !!!!!!!')
            print('-------------------------------------------------------------')
            continue # Volta o loop do começo
    else :
        print('!!!!!!! ---- TAMANHO ou CÓDIGO inválido(s) ---- !!!!!!!')
        print('-------------------------------------------------------------')
        continue # Volta o loop do começo
    
    
    maisAlgo = input('Deseja mais alguma coisa ? (S/N) ')
    if(maisAlgo.upper() == 'N') :
        break # Sai do LOOP
    else :
        continue # Volta o loop do começo
    
print('A sua conta deu : R$ {}'.format(valor)) # Mostra o resultado no console