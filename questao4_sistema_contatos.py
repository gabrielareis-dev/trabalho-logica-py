# Mensagem de boas vindas
print("Bem vindo a lista de contatos da Gabriela Loura")

lista_contatos = []

id_global = 5174948

# Função para cadastrar contatos 
def cadastrar_contato(id):
    print("\n--- CADASTRAR CONTATO ---")

    nome = input("Digite o nome do contato: ")
    atividade = input("Digite a atividade do contato: ")
    telefone = input("Digite o telefone do contato: ")

    # Criação do dicionário
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    # Adiciona cópia do dicionário na lista
    lista_contatos.append(contato.copy())

    print("Contato cadastrado com sucesso!")

# Função para consultar contatos
def consultar_contatos():
 
    while True:
        print("\n--- CONSULTAR CONTATOS ---")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Atividade")
        print("4. Retornar ao menu")

        opcao = input("Escolha: ")

        # Consultar todos os contatos
        if opcao == "1":
            if not lista_contatos:
                print("Nenhum contato cadastrado.")
            else:
                for contato in lista_contatos:
                    print(contato)

        # Consultar por ID
        elif opcao == "2":
             try:
                busca_id = int(input("Digite o id: "))
                encontrado = False
                for contato in lista_contatos:
                    if contato["id"] == busca_id:
                        print(contato)
                        encontrado = True
                        break
                if not encontrado:
                    print("Id não encontrado.")
             except ValueError:  
                    print("Digite um número válido.")

         # Consultar por atividade
        elif opcao == "3":
            atividade_busca = input("Digite a atividade:").strip().lower()
            encontrados = False
            for contato in lista_contatos:
                if contato["atividade"].lower() == atividade_busca:
                    print(contato)
                    encontrados = True
            if not encontrados:
                print("Nenhum contato encontrado com essa atividade.")

        # Voltar ao menu principal
        elif opcao == "4":
            return
        else:
            print("Opção inválida.")


# Função para remover um contato pelo id
def remover_contato():

    while True:
        try:
            remove_id = int(input("Digite o id do contato que deseja remover: "))
            for contato in lista_contatos:
                if contato["id"] == remove_id:
                    lista_contatos.remove(contato)
                    print("Contato removido com sucesso!")
                    return
            print("Id inválido.")
        except ValueError:
            print("Digite um número válido.")

# Menu principal
while True:
    print("\n----------- MENU PRINCIPAL -----------")
    print("1. Cadastrar Contato")
    print("2. Consultar Contato")
    print("3. Remover Contato")
    print("4. Encerrar Programa")

    opcao = input("Escolha a opção desejada: ")

    if opcao == "1":
        cadastrar_contato(id_global)
        id_global += 1
    elif opcao == "2":
        consultar_contatos()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida.")