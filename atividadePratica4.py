id = 0
listaFuncionario = []

# ----- Inicio Cadastrar Funcionario -----
def cadastrarFuncionario(idFunc):
    try:
        nomeFunc = input('Qual o nome do funcionario ? ')
        setorFunc = input('Qual o setor que o funcionario trabalha ? ')
        salarioFunc = int(input('Qual o salario do funcionario ? '))
        funcionario = {
            "id": idFunc,
            "nome": nomeFunc,
            "setor": setorFunc,
            "salario": salarioFunc,
        }
        listaFuncionario.append(funcionario.copy())
    except ValueError:
        print('Digite valores corretos')
# ----- Fim Cadastrar Funcionario -----


# ----- Inicio Consultar Funcionarios -----
def consultarFuncionarios():
    while True:
        try:
            print('1 - Consultar todos os Funcionarios')
            print('2 - Consultar funcionario por id')
            print('3 - Consultar funcionarios por setor')
            print('4 - retornar')
            op = int(input('Quais das 4 opções deseja ? '))

            if op == 1:
                consultarTodosFuncionarios(listaFuncionario)
                continue
            elif op == 2:
                try:
                    id = int(input('Digite o id do funcionario desejado : '))
                    consultarFuncionariosId(listaFuncionario, id)
                    continue
                except ValueError:
                    print('Digite somente valores válidos')
            elif op == 3:
                setor = input('Digite o setor do funcionario desejado : ')
                consultarFuncionariosSetor(listaFuncionario, setor)
                continue
            elif op == 4:
                break
        except ValueError:
            print('Digite uma opção válida')
# ----- Fim Consultar Funcionarios -----


# ----- Inicio Consultar todos os funcionarios -----
def consultarTodosFuncionarios(lista):
    print()
    print('Todos os funcionarios----------------------------------------------------')
    for funcionario in lista:
        print('Seu identificador é : {} . O(A) {} trabalha no setor de {} e ganha R${:.2f} por mês.'.format(
          funcionario['id'],  funcionario['nome'], funcionario['setor'], funcionario['salario']))
    print('Todos os funcionarios----------------------------------------------------')
    print()
# ----- Fim Consultar todos os funcionarios -----


# ----- Inicio Consultar funcionarios por Id -----
def consultarFuncionariosId(lista, id):
    print()
    print('Funcionarios por ID----------------------------------------------------')
    for funcionario in lista:
        if funcionario['id'] == id:
            print('O/A {} trabalha no setor de {} e ganha R${:.2f} por mês.'.format(
                funcionario['nome'], funcionario['setor'], funcionario['salario']))
    print('Funcionarios por ID----------------------------------------------------')
    print()
# ----- Fim Consultar funcionarios por Id -----


# ----- Inicio Consultar funcionarios por Setor -----
def consultarFuncionariosSetor(lista, setor):
    print()
    print('Funcionarios por Setor----------------------------------------------------')
    for funcionario in lista:
        if funcionario['setor'].upper() == setor.upper():
            print('O/A {} trabalha no setor de {} e ganha R${:.2f} por mês.'.format(
                funcionario['nome'], funcionario['setor'], funcionario['salario']))
    print('Funcionarios por Setor----------------------------------------------------')
    print()
# ----- Fim Consultar funcionarios por setor -----


# ----- Inicio Remover funcionarios por Código -----
def removerFuncionario(lista):
    id = int(input('Qual o ID do funcionario que deseja remover ? '))
    for funcionario in lista:
        try:
            if funcionario['id'] == id:
                lista.remove(funcionario)
                print()
                print('------------------------------')
                print()
                print('Funcionário removido com sucesso !!!')
                print()
                print('------------------------------')
                break
        except ValueError:
            print('Digite valores válidos')
    print()
    print('------------------------------')
    print()
    print('Todos os Funcionarios')
    for funcionario in lista:
        print('Seu identificador é : {} . O(A) {} trabalha no setor de {} e ganha R${:.2f} por mês.'.format(
          funcionario['id'],  funcionario['nome'], funcionario['setor'], funcionario['salario']))
    print('------------------------------')
    print()
# ----- Fim Remover funcionarios por Código -----


# ----- MAIN -----
while True:
    id += 1
    print('-----------------------------------------------------------------------------')
    print('Bem vindo ao controle de funcionarios do Rafael Aparecido Gonçalves da Silva')
    print('-----------------------------------------------------------------------------')
    print('-------- Menu Principal --------')
    print('1 - Cadastrar funcionario')
    print('2 - Consultar funcionario')
    print('3 - Remover funcionario')
    print('4 - Sair')
    print('-----------------------------------------------------------------------------')
    try:
        op = int(input('Qual das opções deseja ? '))
        if op == 1:
            cadastrarFuncionario(id)
            continue
        elif op == 2:
            consultarFuncionarios()
            continue
        elif op == 3:
            removerFuncionario(listaFuncionario)
            continue
        elif op == 4:
            break
    except ValueError:
        print('Digite somente valores válidos')
        continue
    
