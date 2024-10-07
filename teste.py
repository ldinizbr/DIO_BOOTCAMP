# Importante função
from datetime import datetime


# data_hora = ""
# data_op =""
# hora_op =""

data_hora = datetime.now()
data_op = data_hora.strftime("%d/%m/%Y")
hora_op = data_hora.strftime("%H:%M:%S")
print(f"hora = {hora_op}")
print(f"dia = {data_op}")