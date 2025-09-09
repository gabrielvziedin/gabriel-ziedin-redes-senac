# Nível 3: Input de terminal + atribuição de variáveis + montagem de dicionário

### Exercício 3.1

# **Pergunta:** Peça ao usuário seu nome, idade e cidade. Armazene essas informações em um dicionário e exiba-o.

'''
nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
cidade = input("Informe a sua cidade: ")

pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

print("---")
print("Nome..: ", pessoa["nome"])
print("Idade.: ", pessoa["idade"])
print("Cidade: ", pessoa["cidade"])
'''

### Exercício 3.2

# **Pergunta:** Solicite o nome de um produto, seu preço e quantidade em estoque. Crie um dicionário com essas informações e imprima.

lista_produto = []

# Produto 1
resposta = "S"
while(resposta == "S"):
    nome_prod = input("Informe o nome do produto: ")
    preco = float(input("Informe p preço do produto: "))
    qtd_estoque = int(input("Informe a quantidade em estoque: "))

    produto = {"nome": nome_prod, "preco": preco, "estoque": qtd_estoque}

    lista_produto.append(produto)
    resposta = input("Adicionar novo produto? [S/n]: ")

# Saída
print(lista_produto)
