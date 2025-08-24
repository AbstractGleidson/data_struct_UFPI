import matplotlib.pyplot as plt 

def frequency_graph(frequency: list, n: int):
    fig, ax = plt.subplots(figsize=(5, 3), layout="constrained") # Especificacoes de layout e tamanho
    
    category = []
    values = []
    
    # Limita a quantidade de categorias 
    if n > 10:
        n = 10
    
    for i in range(n):
        category.append(frequency[i][0])
        values.append(frequency[i][1]) 

    ax.set_title("Frêquencia das palavras") # titulo do grafico
    ax.bar(category, values)
    plt.show() # Mostra o grafico criado