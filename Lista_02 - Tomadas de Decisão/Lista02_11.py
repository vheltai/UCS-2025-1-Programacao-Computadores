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
# entrada de dados:
peso = float (input ("Entre com o peso [kg]: "))
altura = float (input ("Entre com a altura [m]: "))

# Calculo do IMC:
imc = peso / (altura**2)

# Classificação corporeo

if (imc < 20):
    classificacao = "Abaixo do Peso"
if (imc >= 20 and imc < 25):
    classificacao = "Peso Normal"
if (imc >= 25 and imc < 30):
    classificacao = "Sobre Peso"
if (imc >= 30 and imc < 40):
    classificacao = "Obeso"
if (imc >= 40):
    classificacao = "Obeso Morbido"

print (f"Seu IMC: {imc:.2f} - {classificacao}")
