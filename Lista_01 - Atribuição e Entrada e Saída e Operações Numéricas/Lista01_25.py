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

# ENTRADA
materia1 = float(input("Entre com a nota da materia1: "))
materia2 = float(input("Entre com a nota da materia2: "))
materia3 = float(input("Entre com a nota da materia3: "))

# PROCESSAMENTO
media = (materia1 + materia2 + materia3) / 3

# SAIDA
print (media)
print (media > 7)
