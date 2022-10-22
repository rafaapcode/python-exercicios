# ----- Inicio Metragem Limpeza -----
def metragem_limpeza():
    valor = 0
    while True:
        try:
            metragem = int(input('Qual a metragem em m2 da casa ? '))
            if 30 <= metragem < 300 :
                valor = 60 + 0.3 * metragem
                break
            elif 300 <= metragem < 700 :
                valor = 120 + 0.5 * metragem
                break
            else :
                print('!!!!------- ERROR -------!!!!')
                print('!!!! Casas menores que 30 m2 ou maiores ou igual a 700 m2 não são aceitas. !!!!')
                print('!!!!------- ERROR -------!!!!')
        except ValueError:
            print('!!!!------- ERROR -------!!!!')
            print('!!!! Digite somente números !!!!')
            print('!!!!------- ERROR -------!!!!')
    
    return valor
# ------  Fim Metragem Limpeza ------

# ----- Inicio Tipo Limpeza -----
def tipo_limpeza():
    tipo = 1
    while True:
        try:
            print('Temos 2 tipos de limpeza : Básica (B) e Completa (C)')
            tipoLimpeza = input('Qual tipo de limpeza deseja ? ')
            if tipoLimpeza.upper() == 'B':
                break
            elif tipoLimpeza.upper() == 'C':
                tipo = 1.30
                break
            else :
                print('!!!!------- ERROR -------!!!!')
                print('!!!! Digite valores válidos (B ou C) !!!!')
                print('!!!!------- ERROR -------!!!!')
                continue
        except ValueError :
            print('Digite valores válidos')
            continue
    return tipo     
# ----- Fim Tipo Limpeza -----

# ----- Inicio Adicional Limpeza -----
def adicional_limpeza():
    valor = 0
    while True :
        try:
            print('0 - Não desejo mais nada')
            print('1 - Passar 10 peças de roupa (R$ 10,00)')
            print('2 - Limpeza de 1 Forno/Microondas (R$ 12,00)')
            print('3 - Limpeza de 1 Geladeira/Freezer (R$ 20,00)')
            op = int(input('Deseja mais alguma coisa ? '))
            
            if op == 0 :
                break
            elif op == 1 :
                valor += 10
                continue
            elif op == 2 :
                valor += 12
                continue
            elif op == 3 :
                valor += 20
                continue
            else :
                print('!!!!------- ERROR -------!!!!')
                print('!!!! Digite uma das opções mostrada no menu !!!!')
                print('!!!!------- ERROR -------!!!!')
                continue  
        except ValueError:
            print('!!!!------- ERROR -------!!!!')
            print('!!!! Digite valores corretos !!!!')
            print('!!!!------- ERROR -------!!!!')
    return valor
# ----- Fim Adicional Limpeza -----


# ------- MAIN -------
print('Bem-vindo ao Programa de Serviços de Limpeza do Rafael Aparecido Gonçalves da Silva')
print('----- Menu 1 de 3 Metragem Limpeza -----')
valorMetragemCasa = metragem_limpeza()
print('----------------------------------------')
print('----- Menu 2 de 3 Tipo Limpeza -----')
tipolimpeza = tipo_limpeza()
print('----------------------------------------')
print('----- Menu 3 de 3 Adicional Limpeza -----')
adicionalLimpeza = adicional_limpeza()
print('----------------------------------------')
print('**********************************************')
print('Total ((Metragem : R$ {} * Tipo: R$ {}) + Adicional: R$ {}): R$ {:.2f}'.format(valorMetragemCasa, tipolimpeza, adicionalLimpeza, (valorMetragemCasa * tipolimpeza) + adicionalLimpeza))
print('**********************************************')