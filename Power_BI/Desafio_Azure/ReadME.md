Alterei o nome das colunas:
Fname => Nome
Lname => Sobre_nome
Salary => Salario
Sex => Sexo
Dno => N_departamento

Apagado a coluna azure_company.departament

Alterado tipo da coluna Salario para decimal fixo

Na coluna Sexo foi substituído:
M => Masculino
F => Feminino

Verificado um valor nulo no Super_ssn
O que ocorre é que o valor nulo ocorre porque o colaborador é o gerente. Observado que o Ssn dele aparece no Super_ssn de outros colaboradores.

Para dividir a coluna de endereço, substiui - por _ em Fire-Oak
Renomeado para End_Num, End_Logr e End_Cid
Removido coluna de TX, pois todos tem a mesma característica.

Em Super_ssn, subistitui null por vazio

--------------------------

Na tabela departamento.

Removido as colunas 
Mgr_ssn e Mgr_start_date, pois não vão agregar na avaliação.

Mescla de consultas em uma nova tabela. 
Realizado Acrescentar e Mesclar.
em Acrescentar, ele adicionou as colunas que de departament em employee, com novas linhas com valores nulos.
Mesclar acrescenta as colunas combinando com as informações existentes, sem criar novas linhas e valores nulos.





