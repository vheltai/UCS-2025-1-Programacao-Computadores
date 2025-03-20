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

consumo = int (input("Entre com o consumo de energia [kWh]: "))
tipo = input ("Entre com o tipo de instalação [R - Residencial, C - Comercial ou I - Industrial]: ")

if (tipo == "C" or tipo == "c"):
    tipoInst = "Comercial"
    if (consumo <= 1000):
        valorTarifa = 0.55
    else:
        valorTarifa = 0.60

if (tipo == "R" or tipo == "r"):
    tipoInst = "Residencial"
    if (consumo <= 500):
        valorTarifa = 0.40
    else:
        valorTarifa = 0.65
        
if (tipo == "I" or tipo == "i"):
    tipoInst = "Industrial"
    if (consumo <= 5000):
        valorTarifa = 0.55
    else:
        valorTarifa = 0.60

valorConsumo = consumo * valorTarifa

print (f"-------- ANEL ENERGIA ELETRICA LTDA ------------")
print (f"Tipo de Instalação: {tipoInst}")
print (f"Consumo: {consumo} kwh")
print (f"Valor da energia: R${valorTarifa:.2f} / kwh")
print (f"VALOR TOTAL: R${valorConsumo:.2f} ")
