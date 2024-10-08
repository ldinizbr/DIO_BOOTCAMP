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

while True:

    
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

        cliente.update({cpf: dados_cliente})
        print(cliente)
        print(len(cliente))

    menu = input("\nSair? (S/N)").upper()
    print(menu)

    if menu == "S":
        break



# contatos = {
#     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
#     "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#     "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
#     "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
# }

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

