# ****************************************************************************
# Universidade Cruzeiro do Sul - Campus Santo Amaro
# Curso: Analise Desenvolvimento de Sistemas - 1º e 4º Semestre
# Disciplina: Programação de Computadores - Professor Vinicius Heltai
# Autor:        Vinicius Heltai
# Data:         1º Semestre de 2025
# Versão:       1.0
# Descrição:    Lista_02 - Tomada de Decisão
# Repositório:  https://github.com/vheltai/UCS-2025-1-Programacao-Computadores 
# Licença:      MIT
# ****************************************************************************

valor1 = int (input("Entre com o valor 1: "))
valor2 = int (input("Entre com o valor 2: "))

if (valor1 > valor2):
    print (f"{valor1} é maior que {valor2}")

if (valor1 < valor2):
    print (f"{valor1} é menor que {valor2}")

if (valor1 == valor2):
    print (f"{valor1} é igual que {valor2}")





if (valor1 == valor2):
    print (f"{valor1} é igual que {valor2}")
else:
    if (valor1 > valor2):
        print (f"{valor1} é maior que {valor2}")
        
    if (valor1 < valor2):
        print (f"{valor1} é menor que {valor2}")




if (valor1 > valor2):
    oper = "maior"

if (valor1 < valor2):
    oper = "menor"

if (valor1 == valor2):
    oper = "igual"

print (f"{valor1} é {oper} que {valor2}")
        
