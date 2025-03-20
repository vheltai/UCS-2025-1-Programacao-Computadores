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
valor3 = int (input("Entre com o valor 3: "))

if (valor1 > valor2 and valor1 > valor3):
    print (f"{valor1} é maior que {valor2} e {valor3}")
if (valor2 > valor1 and valor2 > valor3):
    print (f"{valor2} é maior que {valor1} e {valor3}")
if (valor3 > valor1 and valor3 > valor2):
    print (f"{valor3} é maior que {valor1} e {valor2}")

if (valor1 < valor2 and valor1 < valor3):
    print (f"{valor1} é menor que {valor2} e {valor3}")
if (valor2 < valor1 and valor2 < valor3):
    print (f"{valor2} é menor que {valor1} e {valor3}")
if (valor3 < valor1 and valor3 < valor2):
    print (f"{valor3} é menor que {valor1} e {valor2}")




if (valor1 > valor2 > valor3):
    print (f"{valor1} é maior que {valor2} e {valor3}")
if (valor2 > valor1 > valor3):
    print (f"{valor2} é maior que {valor1} e {valor3}")
if (valor3 > valor1 > valor2):
    print (f"{valor3} é maior que {valor1} e {valor2}")

if (valor1 < valor2 < valor3):
    print (f"{valor1} é menor que {valor2} e {valor3}")
if (valor2 < valor1 < valor3):
    print (f"{valor2} é menor que {valor1} e {valor3}")
if (valor3 < valor1 < valor2):
    print (f"{valor3} é menor que {valor1} e {valor2}")
