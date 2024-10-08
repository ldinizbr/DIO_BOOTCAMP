# # Importante função
# from datetime import datetime


# # data_hora = ""
# # data_op =""
# # hora_op =""

# # data_hora = datetime.now()
# # data_op = data_hora.strftime("%d/%m/%Y")
# # hora_op = data_hora.strftime("%H:%M:%S")
# # print(f"hora = {hora_op}")
# # print(f"dia = {data_op}")
cliente={}
contas_cadastradas = {}
AGENCIA = "0001"

# ----------------------------------- Função cadastro de conta ----------------------------------------
# Esta função vai receber o número da AGENCIA (uma constante), recebe o dicionário com as contas cadastradas
# e o dicionário de cliente cadastrdos. Vai retornar o dicionário contas_cadastradas com a conta criada.

def cadastro_conta(AGENCIA, contas_cadastradas, cliente):

    print(cliente)

    cpf_cadastrado = input("Digite seu CPF:").replace(" ","").replace(".", "").replace("-", "").replace("_", "")
    
    if cpf_cadastrado in cliente:

        if contas_cadastradas == {}:
            n_conta=1
            print("primeira")
        else:
            lista_contas = list(contas_cadastradas.keys())
            n_conta = max(lista_contas)+1 # Número da conta sequencial. Procura a conta de maior valor.

        contas_cadastradas[n_conta]={"nome_cliente":cliente[cpf_cadastrado]["nome"],
        "agencia":AGENCIA}
        
        print(contas_cadastradas)

        print("Cadastro concluído com sucesso!")

        
    else:
        print("Falha!! CPF não cadastrado.")

    return contas_cadastradas

#  ------------------------------ Fim função cadastra conta -----------------------------------


while True:

    menu = int(input("1 cadastro clinete, 2 castro conta, 3 sair.\n=> "))

    if menu == 1:
            
        cpf = input("Digite seu CPF:").replace(" ","").replace(".", "").replace("-", "").replace("_", "")
        print(f"CPF só números é {cpf}")

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

            cliente[cpf] = dados_cliente
            # cliente.update({cpf: dados_cliente})
            print(cliente)
            print(len(cliente))
    elif menu == 2:
        cadastro_conta(AGENCIA, contas_cadastradas, cliente)
    else:
        break


# testes ================================
# contatos = {
#     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
#     "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#     "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
#     "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
# }


# resultado = list(contatos.keys())  # dict_keys(['guilherme@gmail.com'])
# print(resultado)
# print(len(contatos))
# for chave in contatos:
#     print(chave, contatos[chave])

# print("=" * 100)

# for chave, valor in contatos.items():
#     print(chave, valor)

# contatos = {"leo": {"nome": "Leo01", "telefone": "3333"}}

# contatos.update({"raquel": {"nome": "Raquel","telefone":"4444"}})
# print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

# contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
# print(contatos)


# # buscar o maior valor de conta -----------------------------------------------------------------
# dicionario_contas = {
#     111: {"agencia": "0001", "conta": 1, "nome": "Leo"},
#     222: {"agencia": "0001", "conta": 2, "nome": "Lis"},
#     333: {"agencia": "0001", "conta": 4, "nome": "Yan"},
#     444: {"agencia": "0001", "conta": 5, "nome": "Pedro"}
# }

# cliente = {
#     111: {"telefone": "0001", "conta": 1, "nome": "Leo"},
#     222: {"telefone": "0001", "conta": 2, "nome": "Lis"},
#     333: {"telefone": "0001", "conta": 4, "nome": "Yan"},
#     444: {"telefone": "0001", "conta": 5, "nome": "Pedro"}
# }

# print(dicionario_contas)
# cpf_cadastrado=333

# nome_conta = cliente[cpf_cadastrado]["nome"]
# print(nome_conta)


# #lista_contas = list(dicionario_contas["conta" for cpf in lista_contas.values()])
# lista_contas = [dados["conta"] for dados in dicionario_contas.values()]
# print(lista_contas)
# print(max(lista_contas))

# #------------------------------------------------------------------------------------------



# dicionario_contas[cpff] = dados_conta

# print(dicionario_contas)

# dados_conta["agencia"] = "0001"
# dados_conta["n_conta"] = 2
# dados_conta["nome"] = "lis"
# cpff = 222

# dicionario_contas[cpff] = dados_conta

# print(dicionario_contas)
# ##
# dados_conta["agencia"] = "0001"
# dados_conta["n_conta"] = 2
# dados_conta["nome"] = "lis"
# cpff = 222

# dicionario_contas[cpff] = dados_conta

# print(dicionario_contas)



#         lista_contas = list(conta["conta" for cpf in dados_conta.values()])

#         dados_conta["conta"] = max(lista_contas)+1

# # Dicionário de contas - Como localizar a chave correspondete de um diconário interno. ------
# dicionario_contas = {
#     111: {"agencia": "0001", "conta": 1, "nome": "Leo"},
#     222: {"agencia": "0001", "conta": 2, "nome": "Lis"},
#     333: {"agencia": "0001", "conta": 4, "nome": "Yan"},
#     444: {"agencia": "0001", "conta": 5, "nome": "Pedro"}
# }

# lista_chaves=list(dicionario_contas.keys())
# print(list)

# # Valor da conta que você está procurando
# conta_procurada = 4
# Dicionário de contas
# contas_cadastradas = {
#     111: {"agencia": "0001", "conta": 1, "nome": "Leo"},
#     222: {"agencia": "0001", "conta": 2, "nome": "Lis"},
#     333: {"agencia": "0001", "conta": 4, "nome": "Yan"},
#     444: {"agencia": "0001", "conta": 5, "nome": "Pedro"}
# }

# def conta(agencia, conta, cliente):
#     # Aqui você acessa o dicionário corretamente
#     lista_contas = list(contas_cadastradas.keys())
#     print(lista_contas)

# # Chamada da função com valores de exemplo
# conta("0001", 1, "Leo")

# # Encontrar a chave (CPF) correspondente à conta
# for cpf, dados in dicionario_contas.items():
#     if dados["conta"] == conta_procurada:
#         print(f"A chave correspondente à conta {conta_procurada} é: {cpf}")
#         break

# #------------------------------------------------------------------------------------------