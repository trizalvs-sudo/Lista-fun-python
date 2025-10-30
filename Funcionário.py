lista_funcionarios = []

def cadastrar_funcionario():
    nome_funcionario = str(input("Digite o nome do funcionário: "))
    cargo_funcionario = str(input("Digite o cargo do funcionário: "))
    salario_funcionario = float(input("Digite o salário do funcionário: "))
    data_admissao = str(input("Digite a data de admissão do funcionário (yyyy-mm-dd): "))

    funcionario = ({
        "nome": nome_funcionario,
        "cargo": cargo_funcionario,
        "salario": salario_funcionario,
        "data_admissao": data_admissao
    })

    print("Funcionario adicionado!")

    lista_funcionarios.append(funcionario)


def listar_funcionarios():
    for funcionarios in lista_funcionarios:
        print(f"nome: {funcionarios["nome"]}")
        print(f"cargo: {funcionarios["cargo"]}")
        print(f"salário: {funcionarios["salario"]}")
        print(f"data de admissão: {funcionarios["data_admissao"]}")


def buscar_funcionario():
    busca_nome_funcionario = input("Digite o nome do funcionário q deseja buscar: ")
    encontrado = False

    for funcionario in lista_funcionarios:
        if funcionario["nome"].lower() == busca_nome_funcionario.lower():
            print("Dados do funcionário: \n")
            print(f"Nome: {funcionario["nome"]}")
            print(f"Cargo: {funcionario["cargo"]}")
            print(f"Salário: R$ {funcionario["salario"]:.2f}")
            encontrado = True
            break

        if not encontrado:
            print("Funcionário não encontrado")


def media_salarial():
    soma_salarios = 0
    for funcionario in lista_funcionarios:
        soma_salarios += funcionario["salario"]

    media = soma_salarios / len(lista_funcionarios)

    print(f"\nMédia salarial: R$ {media:.2f}")

    

def menu():
    while True:
        print("Bem vindo ao gerenciamento de funcionários")
        print("\nEscolha um das opções do menu:\n")
        print("1) adicionar um novo funcionario")
        print("2) Listar todos os funcionarios")
        print("3) Buscar funcionário")
        print("4) Média salarial")
        print("0) Sair")

        opcao = input("Escolha: ")
        
        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            buscar_funcionario()
        elif opcao == "4":
            media_salarial()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção invalida, digite novamente.")

menu()

