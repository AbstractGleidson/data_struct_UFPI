import sys
from pathlib import Path
from Text import Text
from frequency_graph import frequency_graph as graph
from widget import mainMenu, clear

# sys.argv[0] - eh o nome do arquivo 
path = Path.home() #Pasta raiz, exemplo: "C:\Users\\Name\"

print(path)

try: 
    path = path / sys.argv[1] # Caminho passado por linha de comando
except IndexError:
    print("Nenhum caminho foi passado!")
    path = None 
    
if __name__ == "__main__":
    if path != None:
        try:
            text = Text.read_txt_file(path=path) # Le o arquivo  
            clear()
            print("Arquivo carregado!\n")
            text = Text(text=text)
            
            response = -1
            
            while(response != 4):
                response = mainMenu()
                
                if response == 1:
                    top = int(input("Top palavras: ")) # Quantidade de palavras exibidas
                    graph(text.frequence_word(), top)
                elif response == 2:
                    top = int(input("Top palavras: ")) # Quantidade de palavras exibidas
                    graph(text.frequence_word_not_stopwords(), top)
                elif response == 3:
                    print("Hapax legomenon:")
                    
                    cont = 1
                    for word in text.hapax_legomenon():
                        print(f"{cont} - {word}")
                        cont += 1
                    
            
        except FileNotFoundError: # Se nao achar o arquivo
            print("Arquivo não encontrado!")
        except PermissionError: # Se nao for informado um arquivo
            print("Caminho inválido!")
    
    else:
        print("Caminho inválido!")
    