import random

alunos = {} 

def cadastrar_aluno(nome, notas):
    """Cadastra um novo aluno com uma lista de notas."""
    if nome in alunos:
        print("Aluno já cadastrado.")
    else:
        alunos[nome] = notas
        print(f"Aluno {nome} cadastrado com sucesso!")

def remover_aluno(nome):
    """Remove um aluno do dicionário."""
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno {nome} removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def mostrar_notas(nome):
    """Mostra as notas de um aluno."""
    if nome in alunos:
        print(f"Notas de {nome}: {alunos[nome]}")
    else:
        print("Aluno não encontrado.")

def melhor_aluno():
    """Encontra o aluno com a melhor média."""
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    melhor = max(alunos, key=lambda nome: sum(alunos[nome]) / len(alunos[nome]))
    media = sum(alunos[melhor]) / len(alunos[melhor])
    print(f"Melhor aluno: {melhor} com média {media:.2f}")

def cadastrar_notas():
    """Captura notas do usuário para cadastrar um novo aluno."""
    notas = []
    while True:
        try:
            nota = float(input("Digite uma nota (ou -1 para parar): "))
            if nota == -1:
                break
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    return notas

def menu():
    """Exibe um menu de opções para interagir com o programa."""
    while True:
        print("\n1. Cadastrar aluno")
        print("2. Remover aluno")
        print("3. Mostrar notas do aluno")
        print("4. Mostrar melhor aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")  
        
        if opcao == '1':
            nome = input("Digite o nome do aluno: ")
            notas = cadastrar_notas()
            cadastrar_aluno(nome, notas)
        elif opcao == '2':
            nome = input("Digite o nome do aluno a ser removido: ")
            remover_aluno(nome)
        elif opcao == '3':
            nome = input("Digite o nome do aluno para ver as notas: ")
            mostrar_notas(nome)
        elif opcao == '4':
            melhor_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def main():
    menu()
    print("\nVoce saiu do programa.")

if __name__ == "__main__":
    main()
