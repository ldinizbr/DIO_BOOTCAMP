# def analise_vendas(vendas):
#       # TODO: Calcule o total de vendas e realize a média mensal:
#       total_vendas=sum(vendas)
#       media_vendas=total_vendas/len(vendas)
    
#       return f"{total_vendas}, {media_vendas:.2f}"

# def obter_entrada_vendas():
#       # Solicita a entrada do usuário em uma única linha
#       entrada = input()
#       # TODO: Converta a entrada em uma lista de inteiros:
#       vendas=list(map(int,entrada.split(",")))
    
#       return vendas

# vendas = obter_entrada_vendas()
# print(analise_vendas(vendas))


# ---------------------------------------------------------------------

def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
         print(f"produto={produto}",f". Contage={count}")
        # TODO: Encontre o produto com a maior contagem:
         if count>max_count:
          max_produto=produto
          max_count=count
        
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    #print(entrada)
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    #lista = [item.strip() for item in entrada.split(",")]
    produtos=[item.strip() for item in entrada.split(",")]
    # produtos=list(entrada.strip().split(","))
    print(produtos)
    
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))