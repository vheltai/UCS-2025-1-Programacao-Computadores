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

distancia = float (input("Entre com a distancia [km]: "))

# Maneira 1
if (distancia <= 200):
    print (f"A distancia {distancia:.1f} km total: R${distancia*0.5}")
else:
    print (f"A distancia {distancia:.1f} km total: R${distancia*0.45}")

# Maneira 2
if (distancia <= 200):
    print (f"A distancia {distancia:.1f} km total: R${distancia*0.5}")
if (distancia > 200):
    print (f"A distancia {distancia:.1f} km total: R${distancia*0.45}")

# Maneira 3
if (distancia <= 200):
    preco = 0.50
if (distancia > 200):
    preco = 0.45
print (f"A distancia {distancia:.1f} km total: R${distancia*preco}")

