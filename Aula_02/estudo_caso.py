'''
# Estudo de Caso

## Sistema de Controle de Alunos em uma Academia

## Cenário

Uma academia deseja criar um sistema simples para monitorar seus alunos. Cada aluno tem: **nome**, **idade**, **altura**, **se está ativo na academia (booleano)** e **notas de avaliação física (lista de floats)**. O sistema deve permitir:

- Cadastrar alunos
- Calcular a média das avaliações de cada aluno
- Identificar alunos ativos e inativos
- Mostrar os dados de todos os alunos

'''

def calcular_media(avaliacoes):
    return sum(avaliacoes) / len(avaliacoes)


def exibir_alunos(alunos):
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Altura: {aluno['altura']}")
        print(f"Ativo: {aluno['ativo']}")
        print(f"Média avaliações: {calcular_media(aluno['avaliacoes']):.2f}")
        print("-"*20)


def listar_alunos(alunos):
    ativos = [aluno for aluno in alunos if alunos['ativos']]
    return ativos


alunos = [
    {
        "nome": "Gabriel",
        "idade": 21,
        "altura": 1.74,
        "ativo": False,
        "avaliacoes": [5.5, 6.5, 7.5]
    },
    {
        "nome": "João",
        "idade": 22,
        "altura": 1.78,
        "ativo": True,
        "avaliacoes": [6.5, 7.5, 8.5]
    },
    {
        "nome": "Maria",
        "idade": 23,
        "altura": 1.64,
        "ativo": True,
        "avaliacoes": [7.5, 8.5, 9.5]
    },
]


exibir_alunos(alunos)
