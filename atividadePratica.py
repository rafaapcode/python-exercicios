# inicialização do programa e entrada de dados do usuário
print('Bem vindo a loja do Rafael Aparecido Gonçalves da Silva')
produto = float(input('Qual o valor do produto: '))
quantidade = int(input('Qual a quantidade do produto: '))

# Variáveis para inicializar o valor com Frete, sem frete e também o FRETE
valorSemFrete = 0
valorComFrete = 0
frete = 0

# Condicionais para as diversas condições de quantidade de produtos
if 0 <= quantidade < 11 :
    # Cáculos dos valores e atribuição do frete de acordo com sua quantidade
    frete = 30
    valorSemFrete = (produto * quantidade)
    valorComFrete = valorSemFrete + frete
elif 11 <= quantidade < 101 :
    frete = 60
    valorSemFrete = (produto * quantidade)
    valorComFrete = valorSemFrete + frete
elif 101 <= quantidade < 1001 :
    frete = 120
    valorSemFrete = (produto * quantidade)
    valorComFrete = valorSemFrete + frete
else :
    frete = 240
    valorSemFrete = (produto * quantidade)
    valorComFrete = valorSemFrete + frete


# Print do valor final com e sem frete
print('Valor final sem frete = R$ {:.2f}'.format(valorSemFrete))
print('Valor final com frete = R$ {:.2f} (valor do frete = R$ {})'.format(valorComFrete, frete))