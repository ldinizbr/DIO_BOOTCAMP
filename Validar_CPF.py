cpf_in=input("digite CPF:").replace(".","").replace("-","").replace("_","")
mult=1
cpf_lista=[]
dig_1=0
dig_2=0

for numero in cpf_in: # Gera uma lista apenas com os números do cpf
    numero=int(numero)
    if isinstance(numero, int):
        cpf_lista.append(numero)

print(f"lista do cpf: {cpf_lista}")

for i in range(9):  # Vai calcular o primeiro dígito verificador
    dig_1+=mult*cpf_lista[i]
    print(f"Digito: {cpf_lista[i]}, mult: {mult}, Dxmult: {cpf_lista[i]*mult} e calculo do dig: {dig_1}")
    mult+=1
    
dig_1=dig_1%11
dig_1=0 if dig_1==10 else dig_1
print("-"*10)
print(f"Digito 1 = {dig_1}")

if dig_1!= cpf_lista[9]:
    print("CPF NÃO É VÁLIDO")

else:
    mult=0
    for i in range(10):  # Vai calcular o segundo dígito verificador
        dig_2+=mult*cpf_lista[i]
        print(f"Digito: {cpf_lista[i]}, mult: {mult}, Dxmult: {cpf_lista[i]*mult} e calculo do dig: {dig_2}")
        mult+=1
    
    dig_2=dig_2%11
    print(dig_2%11)
    dig_2=0 if dig_2==10 else dig_2
    print(f"Digito 2 = {dig_2}")
    print(cpf_lista[10])

    if dig_2!= cpf_lista[10]:
        print("CPF NÃO É VÁLIDO")
    else:
        print("CPF VERIFICADO. OK!")
