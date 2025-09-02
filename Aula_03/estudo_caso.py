# Controle de Qualidade na Produção de Refrigerantes (Coca-Cola)

'''

**lotes de produção**

- **Brix (°Bx):** quantidade de açúcar presente, que afeta o sabor.
- **pH:** acidez do produto, fundamental para a conservação e para manter o padrão sensorial.
- **Nível (mL):** volume de líquido dentro da garrafa, que precisa estar dentro da faixa regulamentada.


**faixas de especificação definidas**

1. **Entrada de dados via terminal**: o operador deve informar o lote, a linha de produção e as medições coletadas (Brix, pH e Nível).
2. **Validação automática**: o programa deve comparar cada valor informado com as faixas de especificação.
3. **Identificação de erros**: se uma medição estiver fora do padrão, o sistema deve indicar se o valor está **baixo** ou **alto**.
4. **Relatório final**: ao término da coleta, o sistema deve mostrar quantas inspeções foram realizadas e destacar os registros fora de especificação.

- **Brix:** entre 10,5 e 11,2 °Bx
- **pH:** entre 2,3 e 2,6
- **Nível:** entre 195 e 205 mL

**Desafio Proposto**

1. Construir o **sistema de entrada de dados** usando `input()`.
2. Criar uma **estrutura de armazenamento** adequada (listas e dicionários).
3. Implementar uma função que compare os valores com os limites e registre os erros.
4. Ao final, exibir um **relatório resumido** destacando os lotes e linhas que apresentaram problemas.

'''

# func

###

base = []

###

lote = (int(input("Informe o lote: ")))
linha_prod = (int(input("Informe a linha de produção: ")))

bx = float(input("Informe o Brix (°Bx): "))
ph = float(input("Informe o pH: "))
nivel_ml = float(input("Informe o Nível (mL):"))

###

medicoes = {"bx": bx, "ph": ph, "nivel": nivel_ml}
base.append({"lote": lote, "linha": linha_prod, "medicoes": medicoes})

for i in base:
    print(i)
