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

def inspecao(medicoes):
    validacoes = {"brix": "", "ph": "", "nivel": ""}

    if medicoes["brix"] < 10.5:
        validacoes["brix"] = "baixo"
    elif medicoes["brix"] > 11.2:
        validacoes["brix"] = "alto"
    else:
        validacoes["brix"] = "ok"

    if medicoes["ph"] < 2.3:
        validacoes["ph"] = "baixo"
    elif medicoes["ph"] > 2.6:
        validacoes["ph"] = "alto"
    else:
        validacoes["ph"] = "ok"

    if medicoes["nivel"] < 195:
        validacoes["nivel"] = "baixo"
    elif medicoes["nivel"] > 205:
        validacoes["nivel"] = "alto"
    else:
        validacoes["nivel"] = "ok"

    return validacoes

relatorio = []

resp = 1
while(resp == 1):
    print("---")

    lote = (int(input("Informe o lote: ")))
    linha_prod = (int(input("Informe a linha de produção: ")))

    brix = float(input("Informe o Brix (°Bx): "))
    ph = float(input("Informe o pH: "))
    nivel = float(input("Informe o Nível (mL):"))

    medicoes = {"brix": brix, "ph": ph, "nivel": nivel}
    validacoes = inspecao(medicoes)

    relatorio.append({"lote": lote, "linha": linha_prod, "medicoes": medicoes, "validacoes": validacoes})

    resp = int(input("---\n1. Adicionar novo lote\n2. Exibir relatório (encerrar programa)\n[1/2]?: "))

for i in relatorio:
    print("---")
    print(f"Lote: {i['lote']}\nLinha: {i['linha']}\nMedições:")
    print(f"Brix  = {i['medicoes']['brix']} °Bx ({i['validacoes']['brix']})")
    print(f"pH    = {i['medicoes']['ph']} ({i['validacoes']['ph']})")
    print(f"Nível = {i['medicoes']['nivel']} mL ({i['validacoes']['nivel']})")
