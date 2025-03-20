# ****************************************************************************
# Universidade Cruzeiro do Sul - Campus Santo Amaro
# Curso: Analise Desenvolvimento de Sistemas - 1º e 4º Semestre
# Disciplina: Programação de Computadores - Professor Vinicius Heltai
# Autor:        Vinicius Heltai
# Data:         1º Semestre de 2025
# Versão:       1.0
# Descrição:    Lista_01 - Atribuição e Entrada e Saída e Operações numéricas
# Repositório:  https://github.com/vheltai/UCS-2025-1-Programacao-Computadores 
# Licença:      MIT
# ****************************************************************************

distancia = int (input("Entre com a distancia [km]: "))
tempo = int (input("Entre com o tempo [dia]: "))
diaria = 60
kmRodado = 0.15

valor = distancia * kmRodado + tempo * diaria

print (f"O aluguel de: {tempo} dias e {distancia} km rodado:")
print (f"Diaria:    {tempo} dias x R$ {diaria:.2f}/dia")
print (f"Km Rodado: {distancia} km * R$ {kmRodado:.2f}/km")
print (f"TOTAL: R$ {valor:.2f}")
