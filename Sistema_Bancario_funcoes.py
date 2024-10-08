# Importante função
from datetime import datetime


# Inicialização das variáveis.

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
AGENCIA = "0001"
cliente = {}
contas_cadastradas = {}


# ----------------------------------- Função cadastro de conta ----------------------------------------
# Esta função vai receber o número da AGENCIA (uma constante), recebe o dicionário com as contas cadastradas
# e o dicionário de cliente cadastrdos. Vai retornar o dicionário contas_cadastradas com a conta criada.
def cadastro_conta(AGENCIA, contas_cadastradas, cliente):

    # Busca o CPF do cliente que deseja abrir a conta.
    cpf_cadastrado = input("Digite seu CPF:").replace(" ","").replace(".", "").replace("-", "").replace("_", "")
    
    if cpf_cadastrado in cliente: # Verifica se o CPF está cadastrado.

        if contas_cadastradas == {}: # Avalia se é o primeiro conta.
            n_conta=1
        else:
            lista_contas = list(contas_cadastradas.keys())
            n_conta = max(lista_contas)+1 # Procura a conta de maior valor.

        contas_cadastradas[n_conta]={"nome_cliente":cliente[cpf_cadastrado]["nome"],
        "agencia":AGENCIA}

        print("\n=== Cadastro concluído com sucesso! ===")

    else:
        print("< Falha!! CPF não cadastrado. >")

    return contas_cadastradas
#  ------------------------------ Fim função cadastra conta -----------------------------------

# ----------------------------------- Função cadastro de cliente ----------------------------------------
# Esta função recebe o dicionário com os clientes cadastradas
# Retona ao dicionário atualizado.
def cadastro(cliente):

    cpf = input("Digite seu CPF (somente números): ").replace(" ","").replace(".", "").replace("-", "").replace("_", "")

    if cpf in cliente:
        mensagem = ("< Falha de operação. CPF já cadastrado. >")

    else:
        dados_cliente={}
        
        nome = input("Digite seu nome completo.\n=> ")  
        dados_cliente["nome"] = nome

        telefone = input("Digite o número do telefone com DDD.\n=> ")
        dados_cliente["telefone"] = telefone

        nascimento = input("Digite a data do seu nascimento (dd/mm/aaa).\n=> ")  
        dados_cliente["data_nascimento"] = nascimento

        endereco = input("Digite seu endereço (Rua/Av., nome da rua, nº, bairro, cidade-UF).\n=> ")  
        dados_cliente["endereco"] = endereco

        cliente[cpf] = dados_cliente
        print("\n=== Cadastro realizado com sucesso! ===\n")

    return cliente
#  ------------------------------ Fim função cadastro de cliente -----------------------------------

# ----------------------------------- Função saque --------------------------------------------------
# Esta função vai subtrair o valor informado do saldo existente.
# A quantidade de saque é limitado e o valor máximo também, conforme variavel 'numero_saques' e constante LIMITE_SAQUES.
# Recebe a variável extrato para atualizar a operação realizada.
# Atualiza e retorna saldo, numero_saques, extrato e mensagem do resultado da operação.
def saque(*,saldo, limite, numero_saques,limite_saque,extrato):
    mensagem=""

    valor = float(input("Informe o valor do saque: "))
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        mensagem = "< Operação falhou! Você não tem saldo suficiente. >\n"
        mensagem += f"Saldo atual é R$ {saldo:.2f}"

    elif excedeu_limite:
        mensagem = "< Operação falhou! O valor do saque excede o limite. >\n"
        mensagem += f"< Limite por saque é R$ {limite:.2f} >"

    elif excedeu_saques:
        mensagem = "< Operação falhou! Número máximo de saques excedido. >"

    elif valor > 0:

        data_hora = datetime.now()

        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\t{data_hora.strftime("%d/%m/%Y")}\t{data_hora.strftime("%H:%M:%S")}\n"
        numero_saques += 1
        mensagem = "=== Saque realizado com sucesso! ==="

    else:
        mensagem=("< Operação falhou! O valor informado é inválido. >")

    return saldo,numero_saques,extrato,mensagem
#  ------------------------------ Fim função cadastro de cliente -----------------------------------

# --------------------------------------- Função deposito -------------------------------------------
# Esta função adiciona o valor informado no saldo existente.
# Atualiza e retorna saldo e extrato.

def deposito(saldo,extrato,/):
    mensagem=""
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        data_hora = datetime.now()
        extrato += f"Depósito:\tR$ {valor:.2f}\t{data_hora.strftime("%d/%m/%Y")}\t{data_hora.strftime("%H:%M:%S")}\n"
        mensagem = "\n=== Depósito realizado com sucesso! ==="

    else:
        mensagem = "< Operação falhou! O valor informado é inválido. >"

    return saldo,extrato,mensagem
#  ------------------------------ Fim função cadastro de cliente -----------------------------------

# ----------------------------------- Função extrato ----------------------------------------
# Imprimir o saldo que foi atualizado pelas funções saque e deposito.
# Não retorna valor.
def print_extrato(saldo,/,*,extrato):
    print("\n======================== EXTRATO ========================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================================")
    return
#  ------------------------------ Fim função cadastro de cliente -----------------------------------

# ----------------------------------- Função principal ----------------------------------------
while True: # Loop infinito para o programa rodar contínuo.

    opcao = input(menu)

    if opcao == "d":
        saldo,extrato,mensagem = deposito(saldo,extrato)
        print(mensagem)

    elif opcao == "c":
        cliente = cadastro(cliente)

    elif opcao == "s":
        saldo, numero_saques, extrato, mensagem = saque(
            saldo=saldo,
            limite=limite,
            numero_saques=numero_saques,
            limite_saque=LIMITE_SAQUES,
            extrato=extrato)
        
        print(mensagem)

    elif opcao == "e":
        print_extrato(saldo,extrato=extrato)

    elif opcao == "a":
        cadastro_conta(AGENCIA, contas_cadastradas, cliente)

    elif opcao == "q":
        break

    else: # Quando a entrada não tem uma opção válida.
        print("< Operação inválida, por favor selecione novamente a operação desejada. >")
# ----------------------------------- Fim do Programa ----------------------------------------