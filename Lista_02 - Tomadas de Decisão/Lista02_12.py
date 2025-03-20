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

while (True):
    print ("-------------------------------")

    salarioMedio = 0.00
    percentual = 0
    credito = 0

    salarioMedio = float(input("Entre com o salario medio [R$]: "))

    if (salarioMedio >= 0 and salarioMedio <= 500): percentual = 0
        
    if (salarioMedio > 500 and salarioMedio <= 1000): percentual = 30
        
    if (salarioMedio > 1000 and salarioMedio <= 3000): percentual = 40
        
    if (salarioMedio > 3000): percentual = 50

    credito = salarioMedio * percentual/100

    print (f"Salario Medio: R${salarioMedio:.2f} - Percentual: {percentual}%")
    print (f"Credito R${credito:.2f}")

    sair = input("Digite S para sair ou qualquer tecla para continuar... ")
    if (sair == "S" or sair == "s"):
        break

    
