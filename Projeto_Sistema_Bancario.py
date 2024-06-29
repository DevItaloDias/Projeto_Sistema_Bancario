menu = """

- Sistema Bancario - 

[D] - Deposito
[S] - Saque
[E] - Extrato
[Q] - Sair

"""

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).upper()

    if opcao == "D":
        valor = float(input("Insira o Valor do Deposito: "))

        if valor > 0:
            saldo += valor
            extrato += "Deposito: R${:.2f}\n".format(valor)
            print("Saldo Atual: R${:.2f}".format(saldo))
        else:
            print("O Valor Informado é Inválido.")
    
    elif opcao == "S":
        valor = float(input("Insira o Valor do Saque: "))

        excedeu_valor = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques >= LIMITE_SAQUES

        if excedeu_valor:
            print("O Valor do Saque Excede o Saldo Atual.")
        elif excedeu_limite:
            print("O Valor do Saque Excede o Limite de Saque.")
        elif excedeu_saques:
            print("O Valor do Saque Excede o Limite de Saques Diários.")
        elif valor > 0:
            saldo -= valor
            extrato += "Saque: R${:.2f}\n".format(valor)
            num_saques += 1
            print("Saldo Atual: R${:.2f}".format(saldo))
        else:
            print("O Valor do Saque é Inválido.")

    elif opcao == "E":
        print("="*15 + "EXTRATO" + "="*15)
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print("Saldo: R${:.2f}".format(saldo))
        print("="*37)

    elif opcao == "Q":
        break
    
    else:
        print("Operação Inválida! Por favor, Selecione a Opção Correspondente.")