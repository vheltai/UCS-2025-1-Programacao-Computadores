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

velocidade = int (input("Entre com a velocidade do veiculo [km/h]: "))
limite = 80
margem = 2
valor = 5.00

if (velocidade > limite+margem):
    
    print ("Parabens, você foi multado.. kkkkkkkkk")

    diferenca = velocidade - limite
    multa = diferenca * valor

    print (f"Velocidade: {velocidade} km/h : {diferenca} km/h acima do permitido")
    print (f"Valor da Multa: R$ {multa:.2f}")

else:
    print ("Que pena não foi hoje... me aguarde... bjs CET")
