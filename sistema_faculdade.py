alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso do aluno: ")
    lista_cursos = [aluno["curso"] for aluno in alunos]
    quantidade_curso = lista_cursos.count(curso)
    matricula = f"{curso}{quantidade_curso + 1}"

    alunos.append({ "nome": nome, "email": email, "curso": curso, "matricula": matricula })
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        agrupados = {}

        for aluno in alunos:
            curso = aluno["curso"]
            if curso not in agrupados:
                agrupados[curso] = []
            agrupados[curso].append(aluno)

        for curso, lista in agrupados.items():
            print(f"\nCurso: {curso}")
            for aluno in lista:
                print(f"  - Nome: {aluno['nome']}, E-mail: {aluno['email']}, Matrícula: {aluno['matricula']}")


def atualizar_aluno():
    nome = input("Digite o nome do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            aluno["email"] = input("Digite o novo e-mail: ")
            curso = input("Digite o novo curso: ")
            aluno["curso"] = curso
            lista_cursos = [aluno["curso"] for aluno in alunos]
            quantidade_curso = lista_cursos.count(curso)
            matricula = f"{curso}{quantidade_curso + 1}"
            aluno["matricula"] = matricula
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return
    print("Aluno não encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Atualizar aluno")
        print("4. Remover aluno")
        print("5. Sair")

        opcao = input("Opções: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Tente novamente.")

if __name__ == "__main__":
    main()