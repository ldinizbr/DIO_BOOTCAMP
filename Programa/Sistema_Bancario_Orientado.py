# ----------------------- Criação da classe Cliente --------------------------------------------------
class Cliente:

    # posso criar uma lista para todos cliente criados. Vou criar uma variavel
    lista_de_clientes=[]
    lista_contas=[]
    
    def __init__(self,nome,cpf):
        self.nome=nome
        self.cpf=cpf
        lista_contas=[]
        self.endereco=endereco
        Cliente.lista_de_clientes.append(self) #vou acrescentar cada cliente cirado.

    def __str__(self):
        return f"""
        Nome: {self.nome}
        CPF: {self.cpf}
        """
    def listar_clientes():
        for ccliente in Cliente.lista_de_clientes:
            print(f"Nome: {ccliente.nome} - CPF: {ccliente.cpf}")

# -------------------------// Fim: classe Cliente //--------------------------------------------------

# ----------------------- Criação da classe Conta ------------------------------------------
class Conta:
    def __init__(self):
        #atributos privados (-)
        self.saldo=saldo
        self.numero=numero
        self.agencia=agencia
        self.cliente=cliente
        self.historico=Historico
    # teremos 4 métodos, saldo nova_conta sacar

# -------------------------// Fim: classe Conta //--------------------------------------------------

cliente_leo=Cliente("Leonardo","03662936640")
cliente_lis=Cliente("Lis Paula","1234")
cliente_yan=Cliente("Yan Felipe","5678")
cliente_pedro=Cliente("Pedro","0011")

Cliente.listar_clientes()
            

# class Contas_clientes:

#     # posso criar uma lista para todos cliente criados. Vou criar uma variavel
#     lista_clientes=[]
    
#     def __init__(self) -> None:
#         pass
        
# historico
# #conta
# #saldo, numero, agencia, cliente, historico

# #cliente=> -endereço, -conta, +realizar trasacao, +adicionar uma conta


# #PessoaFisica=> -cpf, -nome, -data_nascimento

