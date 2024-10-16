# Importando bibliotecas.
from abc import ABC
from datetime import datetime


# ----------------------- Criação da classe Cliente --------------------------------------------------
class Cliente:

    # posso criar uma lista para todos cliente criados. Vou criar uma variavel
    #lista_de_clientes=[]
    #lista_contas=[]
    
    def __init__(self,endereco):
        self.endereco=endereco
        self.lista_de_clientes=[]
        self.lista_contas=[]
        # self.nome=nome
        # self.cpf=cpf
        # self.data_nasc=data_nasc
        #Cliente.lista_contas.append(self)
        Cliente.lista_de_clientes.append(self) #vou acrescentar cada cliente cirado.

    def adicionar_conta(self,):
        self.lista_contas.append(conta)

    def realizar_trasacao(self,conta,transacao):
        transacao.registrar(conta)

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

# ----------------------- Criação da classe Conta ------------------------------------------
class Conta:
    def __init__(self,saldo,numero,agencia,cliente,Historico): #
        #atributos privados (-)
        self._saldo = 0
        self._numero = numero
        self._agencia ="0001"
        self._cliente = cliente
        self._historico = Historico()
        self._tipo = True
    # teremos 4 métodos, saldo nova_conta sacar

    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)

    @property
    def saldo(self):
        # print(f"Saldo atual é {self.saldo}")
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @property
    def tipo(self):
        return "Pessoa Física" if self._tipo else "Empresarial"
    
    def alternar_conta(self):
        self._tipo = not self._tipo

    def __str__(self):
         return f"Saldo: {self.saldo} e Tipo: {self.tipo}"
    
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass
            
# ----------------------- Criação da classe PessoaFisica ------------------------------------------
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# ----------------------- Criação da classe ContaCorrente(Conta) ------------------------------------------
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, cpf, limite=500, limite_saques=3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
             if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False
    
     def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# ----------------------- Criação da classe Historico ------------------------------------------
class Historico(self):
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
        {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y"),
            "hora": datetime.now().strftime("%H:%M:%s"),
        }
    )

# ----------------------- Criação da classe Transacao(ABC) ------------------------------------------
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

# ----------------------- Criação da classe Saque(Transacao) ------------------------------------------
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# ----------------------- Criação da classe Deposito(Transacao) ------------------------------------------
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)




# ----------------------- Programa ------------------------------------------
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


