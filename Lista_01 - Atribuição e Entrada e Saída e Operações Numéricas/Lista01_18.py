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
totalVendas = float(input("Entre com o total de vendas [R$]: "))
comissao = float(input("Entre com a comissão de vendas [%]: "))

# PROCESSAMENTO
resultado = totalVendas * comissao/100

# SAIDA
print (f"Total de Vendas R${totalVendas:.2f}, comissão: {comissao:.1f} - R${resultado:.2f}")
