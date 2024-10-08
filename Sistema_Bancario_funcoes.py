# Importante função
from datetime import datetime

menu = """

[c] Cadastro Cliente
[a] Abertura de Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
cliente={}



# regras para cadastro cliente.


# Aprimorar o código agrupando em funções

def cadastro(cliente):

    cpf = input("Digite seu CPF:").replace(" ","").replace(".", "").replace("-", "").replace("_", "")

    if cpf in cliente:
        mensagem = ("Falha de operação. CPF já cadastrado.")
    else:
        # posicao = len(cliente)
        dados_cliente={}
        
        nome = input("Digite seu nome completo.\n=>")  
        dados_cliente["nome"] = nome

        telefone = input("Digite o número do telefone com DDD.\n=>")
        dados_cliente["telefone"] = telefone

        nascimento = input("Digite a data do seu nascimento (dd/mm/aaa).\n=>")  
        dados_cliente["data_nascimento"] = nascimento

        endereco = input("Digite seu endereço (Rua/Av., nome da rua, nº, bairro, cidade-UF).\n=>")  
        dados_cliente["endereco"] = endereco

        cliente.update({cpf: dados_cliente})
        print("\nCadastro realizado com sucesso!\n")

    return cliente

def saque(saldo, limite, numero_saques,LIMITE_SAQUES,extrato):
    mensagem=""

    valor = float(input("Informe o valor do saque: "))
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        mensagem = "Operação falhou! Você não tem saldo suficiente.\n"
        mensagem += f"Saldo atual é R$ {saldo:.2f}"

    elif excedeu_limite:
        mensagem = "Operação falhou! O valor do saque excede o limite.\n"
        mensagem += f"Limite por saque é R$ {limite:.2f}"

    elif excedeu_saques:
        mensagem = "Operação falhou! Número máximo de saques excedido."

    elif valor > 0:

        data_hora = datetime.now()

        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\t{data_hora.strftime("%d/%m/%Y")}\t{data_hora.strftime("%H:%M:%S")}\n"
        numero_saques += 1
        mensagem = "Saque realizado com sucesso!"

    else:
        mensagem=("Operação falhou! O valor informado é inválido.")

    return saldo,numero_saques,extrato,mensagem

def deposito(saldo,extrato):
    mensagem=""
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        data_hora = datetime.now()
        extrato += f"Depósito:\tR$ {valor:.2f}\t{data_hora.strftime("%d/%m/%Y")}\t{data_hora.strftime("%H:%M:%S")}\n"
        mensagem = "Depósito realizado com sucesso!"

    else:
        mensagem = "Operação falhou! O valor informado é inválido."

    return saldo,extrato,mensagem

#saldo,mensagem

def print_extrato(saldo,extrato):
    print("\n======================== EXTRATO ========================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================================")
    return


while True:

    opcao = input(menu)

    if opcao == "d":
        
        saldo,extrato,mensagem = deposito(saldo,extrato)
        print(mensagem)

    elif opcao == "c":
        cliente = cadastro(cliente)

    elif opcao == "s":
        saldo, numero_saques, extrato, mensagem = saque(saldo, limite, numero_saques, LIMITE_SAQUES, extrato)
        print(mensagem)

    elif opcao == "e":
        print_extrato(saldo,extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")