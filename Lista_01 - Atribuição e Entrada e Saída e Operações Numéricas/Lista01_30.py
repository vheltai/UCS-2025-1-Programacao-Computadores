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

distancia = float (input("Entre com a distancia [km]: "))
velocidade = int (input("Entre com a Velocidade Media [km/h]: "))

tempo = distancia / velocidade

print (f"O tempo gasto na viagem é: {tempo} horas")
