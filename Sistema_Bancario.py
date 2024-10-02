# Este programa é para simular um sistema bancário onde teremos 3 operações:
# sacar, depositar e visualizar extrato.
# Regras: permitido 3 saques diários de 500 reais máximo por saque;
# depósito dever ser sempre positivo e devem ser armazenados para serem mostrados no extrato.
# o extrato deve mostrar toda movimentação. Caso esteja em branco devo mostrar a frase
# "Não foram realizadas movimentações"
# os valores devem ser mostrado em R$

# Sistema Bancario V1.0

saldo=0
valor_deposito=0
valor_saque=0

def deposito(saldo,valor_deposito):
    valor_deposito=print("Digite o valor a ser depositado")
    return saldo += valor_deposito

def saque(saldo,valor_saque):
    valor_saque=print("Digite o valor que deseja sacar")
    if valor_saque>500:
        valor_saque=print("Valor de saque acima do limite, digite valor até R$500,00"end="\n")
    elif valor_saque>saldo:
        valor_saque=print(f"Você não tem saldo suficiente, digite valor até R${saldo}"end="\n")
        
    else:
        print("Saque realizado com sucesso")
        return saldo-=valor_saque



