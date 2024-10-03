# Este programa é para simular um sistema bancário onde teremos 3 operações:
# sacar, depositar e visualizar extrato.
# Regras: permitido 3 saques diários de 500 reais máximo por saque;
# depósito dever ser sempre positivo e devem ser armazenados para serem mostrados no extrato.
# o extrato deve mostrar toda movimentação. Caso esteja em branco devo mostrar a frase
# "Não foram realizadas movimentações"
# os valores devem ser mostrado em R$

# Sistema Bancario V1.0

# Importante função
from datetime import datetime

# Iniciando as variáveis.
menu_inicial=  """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
opcao=""

saldo=float(400)
data_hora=0
valor_deposito=float(0)
valor_saque=float(0)
limite_saque=float(500)
valor=0
data_hora=0
extrato=[["Tipo","Valor","Data/horário","Saldo Atual"]]
numero_saque=0


# Definindo a função saque ------------------------------------------------------------------------
def saque(saldo,limite_saque):
    
    if valor_saque>limite_saque:
        mensagem1="Valor acima do limite permitido. Seu limite de cada saque é " + str(limite_saque)
    else:
        mensagem1=""
        
    if valor_saque>saldo:
        mensagem2="Saldo insuficiente. Seu saldo atual é " + str(saldo)
    else:
        mensagem2=""
        
    if mensagem1=="" and mensagem2=="":
        saldo -=valor_saque
        print("Saque realizado com sucesso")
        data_hora=datetime.now()
        data_hora=data_hora.strftime("%d/%m/%Y %H:%M:%S")
        opcao=""
    else:
        print(f"{mensagem1}\n{mensagem2}")
        data_hora=""
        opcao=2
    
    return saldo,data_hora,opcao

# Definindo a função depósito ---------------------------------------------------------------------
def deposito(saldo,valor_deposito):
    
    
    if valor_deposito<=0:
        print("Valores 'zero' ou negativos não são válidos")
        data_hora=""
        opcao=1
    else:
        saldo+=valor_deposito
        print("Depósito realizado com sucesso")
        data_hora=datetime.now()
        data_hora=data_hora.strftime("%d/%m/%Y %H:%M:%S")
        opcao=""   
        
    return saldo,data_hora,opcao


# Programa Bancário. Criando o programa principal ---------------------------------------

# Criando while para rodar programa de forma contínua.
while opcao!=0:

    if opcao=="":# if01 Verificicar se estamos iniciando a operação
        print(menu_inicial)
        opcao=int(input(":"))
    else:# if01
        if opcao==1: # if02 Verfica se o usuário selecionou Depositar
            valor_deposito=float(input("Digite o valor que deseja depositar: "))
            saldo,data_hora,opcao=deposito(saldo,valor_deposito)
            if opcao=="":
                extrato.append(["Depósito",f"R${valor_deposito:.2f}",data_hora,f"R${saldo:.2f}"])
                            
        elif opcao==2:# Opção de saque
            if numero_saque>=3:# verifica a quantidade de de saques
                print("Você já realizou os 3 saques do seu limite diário.\nEscolha outra opção")
                opcao=""
            else:
                valor_saque=float(input("Digite o valor que deseja sacar: "))
                saldo,data_hora,opcao=saque(saldo,limite_saque)
                if opcao=="":
                    extrato.append(["Saque",f"R${valor_saque:.2f}",data_hora,f"R${saldo:.2f}"])
                    numero_saque+=1
            
        elif opcao==3: # Opção de extrato
            if len(extrato)==1:
                print("Não foram realizadas movimentações")
            else:
               for linha in extrato:
                    print(linha)
               opcao=""

        elif opcao==0:# Deseja sair do programa
            break
        
        else:# if02 Nenhuma opção válida foi digitada. Solicitando que digite novamente.
            print("Opção inválida. Digite novamente")
            opcao=int(input(":"))



