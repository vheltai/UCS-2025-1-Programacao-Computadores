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
var1 = float(input("Entre com o valor da var1 (Ex: 2.34): "))
var2 = float(input("Entre com o valor da var2 (Ex: 3.54): "))
var3 = float(input("Entre com o valor da var3 (Ex: 6.23): "))

# PROCESSAMENTO
resultado = var1 + var2 + var3

# SAIDA
print(f"{var1:.2f} + {var2:.2f} + {var3:.2f} = {resultado:.2f}")
print(f"A Soma dos numeros: {var1:.2f}, {var2:.2f} e {var3:.2f} é igual a {resultado:.2f}")
