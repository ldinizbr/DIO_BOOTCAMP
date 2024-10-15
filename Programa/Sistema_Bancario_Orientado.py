# ----------------------- Criação da classe Cliente --------------------------------------------------
class Cliente:

    # posso criar uma lista para todos cliente criados. Vou criar uma variavel
    lista_de_clientes=[]
    #lista_contas=[]
    
    def __init__(self,nome,cpf,endereco,data_nasc):
        self.nome=nome
        self.cpf=cpf
        self.data_nasc=data_nasc
        self.endereco=endereco
        #Cliente.lista_contas.append(self)
        Cliente.lista_de_clientes.append(self) #vou acrescentar cada cliente cirado.

    def adicionar_conta(self,):
        pass

    def __str__(self):
        return f"""
        Nome: {self.nome}
        CPF: {self.cpf}
        """

    @classmethod
    def mostar_clientes(cls):
        for ccliente in cls.lista_de_clientes:
            print(f"Nome: {ccliente.nome} \tCPF: {ccliente.cpf} \tData Nascimento: {ccliente.data_nasc}")
    
    # def mostra_contas():
    #     for cconta in Cliente.lista_contas:
    #         print(f"Nome: {cconta.nome} - CPF: {cconta.cpf}")

# -------------------------// Fim: classe Cliente //--------------------------------------------------

# ----------------------- Criação da classe Conta ------------------------------------------
class Conta:
    def __init__(self,saldo,numero,agencia,cliente,Historico): #
        #atributos privados (-)
        self._saldo=saldo
        self._tipo=True
        self._numero=numero
        self._agencia=agencia
        self._cliente=cliente
        self._historico=Historico
    # teremos 4 métodos, saldo nova_conta sacar

    def saldo(self):
        print(f"Saldo atual é {self.saldo}")

    @property
    def tipo(self):
        return "Pessoa Física" if self._tipo else "Empresarial"
    
    def alternar_conta(self):
        self._tipo = not self._tipo

    def __str__(self):
         return f"Saldo: {self.saldo} e Tipo: {self.tipo}"
        
# -------------------------// Fim: classe Conta //--------------------------------------------------

cliente_leo=Cliente("Leonardo","03662936640","rua leo","11/22/33")
cliente_lis=Cliente("Lis Paula","1234","rua Lis","11/22/33")
cliente_yan=Cliente("Yan Felipe","5678","rua Yan","11/22/33")
cliente_pedro=Cliente("Pedro","0011","rua Pedro","11/22/33")

conta_leo = Conta(111)
conta_liz = Conta(222)

Cliente.mostar_clientes()
#Cliente.mostra_contas()
print(conta_leo)
print(conta_liz)

conta_leo.alternar_conta()
print(conta_leo)

# class Contas_clientes:

#     # posso criar uma lista para todos cliente criados. Vou criar uma variavel
#     lista_clientes=[]
    
#     def __init__(self,pessoa_f=True):
#         pass
        
# historico
# #conta
# #saldo, numero, agencia, cliente, historico

# #cliente=> -endereço, -conta, +realizar trasacao, +adicionar uma conta


# #PessoaFisica=> -cpf, -nome, -data_nascimento

