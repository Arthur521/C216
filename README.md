# Sistema de Gerenciamento de Alunos

Este projeto é um sistema simples em Python para **cadastrar**, **listar**, **atualizar** e **remover** alunos.
Cada aluno possui:

* Nome
* E-mail
* Curso
* Matrícula gerada automaticamente no formato `CURSO1`, `CURSO2` etc., onde `CURSO` é o código do curso informado.

## Funcionalidades

1. **Cadastrar aluno**

   * Solicita nome, e-mail e curso.
   * Gera automaticamente uma matrícula sequencial baseada no curso.
   * Exemplo: se o curso for `GES`, os alunos terão matrículas `GES1`, `GES2`, `GES3`...

2. **Listar alunos**

   * Mostra todos os alunos cadastrados, **agrupados por curso**.

3. **Atualizar aluno**

   * Atualiza os dados de um aluno existente (nome pesquisado como identificador).
   * Caso o curso seja alterado, a matrícula é recalculada.

4. **Remover aluno**

   * Remove um aluno da lista pelo nome.

5. **Menu interativo**

   * Sistema baseado em menu com as opções disponíveis:

     ```
     1. Cadastrar aluno
     2. Listar alunos
     3. Atualizar aluno
     4. Remover aluno
     5. Sair
     ```

---

## Como Executar

1. Certifique-se de ter o **Python 3.x** instalado na sua máquina.
2. Salve o código em um arquivo, por exemplo: `alunos.py`.
3. Execute no terminal:

   ```bash
   python alunos.py
   ```

---

## Exemplo de Uso

### Cadastro de dois alunos no curso GES e um no curso ADM:

```
Digite o nome do aluno: João
Digite o e-mail do aluno: joao@email.com
Digite o curso do aluno: GES
Aluno João cadastrado com sucesso! Matrícula: GES1

Digite o nome do aluno: Maria
Digite o e-mail do aluno: maria@email.com
Digite o curso do aluno: GES
Aluno Maria cadastrado com sucesso! Matrícula: GES2

Digite o nome do aluno: Pedro
Digite o e-mail do aluno: pedro@email.com
Digite o curso do aluno: ADM
Aluno Pedro cadastrado com sucesso! Matrícula: ADM1
```

### Listagem agrupada:

```
Curso: GES
  - Nome: João, E-mail: joao@email.com, Matrícula: GES1
  - Nome: Maria, E-mail: maria@email.com, Matrícula: GES2

Curso: ADM
  - Nome: Pedro, E-mail: pedro@email.com, Matrícula: ADM1
```

---

## Estrutura do Código

* `cadastrar_aluno()`: Cadastra novos alunos e gera matrícula sequencial.
* `listar_alunos()`: Lista alunos agrupados por curso.
* `atualizar_aluno()`: Atualiza dados de alunos existentes.
* `remover_aluno()`: Remove alunos da lista.
* `main()`: Exibe o menu e controla a interação com o usuário.

---

## Requisitos

* Python 3.6 ou superior.
