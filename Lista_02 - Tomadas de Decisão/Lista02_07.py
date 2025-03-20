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

categoria = int (input("Entre com a categoria [1-5]: "))

valor1 = 10.00
valor2 = 15.00
valor3 = 19.00
valor4 = 23.00
valor5 = 27.00

# Maneira 1
if (categoria == 1):
    print (f"Preço R${valor1:.2f}")
if (categoria == 2):
    print (f"Preço R${valor2:.2f}")
if (categoria == 3):
    print (f"Preço R${valor3:.2f}")
if (categoria == 4):
    print (f"Preço R${valor4:.2f}")
if (categoria == 5):
    print (f"Preço R${valor5:.2f}")


# Maneira 2
if (categoria == 1):
    print ("Preço R$ 10,00")
else:
    if (categoria == 2):
        print ("Preço R$ 15,00")
    else:
        if (categoria == 3):
            print ("Preço R$ 19,00")
        else:
            if (categoria == 4):
                print ("Preço R$ 23,00")
            else:
                if (categoria == 5):
                    print ("Preço R$ 27,00")

# Maneira 3
if (categoria == 1):
    print ("Preço R$ 10,00")
elif (categoria == 2):
    print ("Preço R$ 15,00")
elif (categoria == 3):
    print ("Preço R$ 19,00")
elif (categoria == 4):
    print ("Preço R$ 23,00")
elif (categoria == 5):
    print ("Preço R$ 27,00")
