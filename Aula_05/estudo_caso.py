# Estudo de Caso — Sistema de Controle de Alarme com Portas Lógicas

'''
Este estudo de caso expande a ideia de um sistema de alarme em uma fábrica, utilizando **portas lógicas** e simulação em **Python**. O desafio foi dividido em quatro níveis de complexidade, permitindo que o aluno avance passo a passo.

---

## Contexto

Uma fábrica precisa de um **sistema de alarme** que garanta a segurança em situações de risco. O alarme pode ser disparado por diferentes condições, que combinam sensores e controles de emergência.

As entradas possíveis são:

- **F (Fumaça):** 1 se há fumaça, 0 caso contrário.
- **B (Botão de Emergência):** 1 se pressionado, 0 caso contrário.
- **C (Chave de Segurança):** 1 se ativada, 0 caso contrário.
- **M (Movimento):** 1 se detectado movimento em área restrita, 0 caso contrário.

A saída é:

- **Alarme (A):** 1 se deve tocar, 0 caso contrário.
'''

fumaca = 0
botaoEmergencia = 0
chaveSeguranca = 1
movimento = 0

alarme = 0

fumaca = int(input("Tem fumaça? "))
if fumaca == 1 or botaoEmergencia == 1 and chaveSeguranca == 1 or movimento == 1 and chaveSeguranca == 0:
    alarme = 1
    print("Alarme ativo")
else:
    alarme = 0
    print("Alarme inativo")
