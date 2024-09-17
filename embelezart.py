# Função para exibir o menu da agenda
def exibir_menu():
    print("\n--- Agenda ---")
    print("1. Adicionar compromisso")
    print("2. Ver compromissos")
    print("3. Editar compromisso")
    print("4. Remover compromisso")
    print("5. Sair")

# Função para adicionar um compromisso
def adicionar_compromisso(agenda):
    data = input("Digite a data (DD/MM/AAAA): ")
    hora = input("Digite a hora (HH:MM): ")
    descricao = input("Digite a descrição do compromisso: ")
    agenda.append({"data": data, "hora": hora, "descricao": descricao})
    print("Compromisso adicionado com sucesso!")

# Função para visualizar compromissos
def ver_compromissos(agenda):
    if len(agenda) == 0:
        print("Nenhum compromisso agendado.")
    else:
        for i, compromisso in enumerate(agenda):
            print(f"{i+1}. {compromisso['data']} {compromisso['hora']} - {compromisso['descricao']}")

# Função para editar um compromisso
def editar_compromisso(agenda):
    ver_compromissos(agenda)
    indice = int(input("Digite o número do compromisso que deseja editar: ")) - 1
    if 0 <= indice < len(agenda):
        agenda[indice]["data"] = input("Nova data (DD/MM/AAAA): ")
        agenda[indice]["hora"] = input("Nova hora (HH:MM): ")
        agenda[indice]["descricao"] = input("Nova descrição: ")
        print("Compromisso editado com sucesso!")
    else:
        print("Compromisso não encontrado.")

# Função para remover um compromisso
def remover_compromisso(agenda):
    ver_compromissos(agenda)
    indice = int(input("Digite o número do compromisso que deseja remover: ")) - 1
    if 0 <= indice < len(agenda):
        del agenda[indice]
        print("Compromisso removido com sucesso!")
    else:
        print("Compromisso não encontrado.")

# Função para salvar a agenda em um arquivo .txt
def salvar_agenda(agenda):
    with open('agenda.txt', 'w') as arquivo:
        for compromisso in agenda:
            arquivo.write(f"{compromisso['data']} {compromisso['hora']} - {compromisso['descricao']}\n\n")

# Função para carregar a agenda de um arquivo .txt
def carregar_agenda():
    agenda = []
    try:
        with open('agenda.txt', 'r') as arquivo:
            linhas = arquivo.read().strip().split('\n\n')
            for linha in linhas:
                partes = linha.split(' - ', 1)
                if len(partes) == 2:
                    data_hora = partes[0].split(' ', 1)
                    if len(data_hora) == 2:
                        data, hora = data_hora
                        descricao = partes[1]
                        agenda.append({"data": data, "hora": hora, "descricao": descricao})
    except FileNotFoundError:
        pass
    return agenda

# Função principal
def main():
    agenda = carregar_agenda()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_compromisso(agenda)
            salvar_agenda(agenda)
        elif opcao == "2":
            ver_compromissos(agenda)
        elif opcao == "3":
            editar_compromisso(agenda)
            salvar_agenda(agenda)
        elif opcao == "4":
            remover_compromisso(agenda)
            salvar_agenda(agenda)
        elif opcao == "5":
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
