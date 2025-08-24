import nltk.corpus as corpus
import nltk

nltk.download("stopwords") # Faz o download das stopwords usando a api do nltk

class Text:
    stopwords = corpus.stopwords.words("portuguese") # Cria uma list com as stopwords, stop_words e uma variavel static
    
    def __init__(self, text: str):
        self.text = Text.extract_ponctuation(text.lower())

    @staticmethod
    def read_txt_file(path) -> str:
        file = open(path, "r", encoding="UTF-8")  # Abre aquivo no modo leitura 
        text = file.read() # le o arquivo 
        file.close() 
        
        return text # retorna o conteudo do arquivo
    
    # Extrai todas as palavras do texto e retorna uma lista
    def extracts_words_text_list(self) -> list[str]:
        list_words = [] # Lista de palavras
        
        for word in self.text:
            if word not in list_words: # Adiciona a palavra se ela ja nao tiver no testo
                list_words.append(word) 
        
        return list_words
    
    def extracts_words_text_set(self) -> set[str]:
        return set(self.text)
    
    # Retorna uma lista das palavras do texto tirando as stopwords
    def extract_stopwords(self) -> list[str]:
        return [word for word in self.text if word not in Text.stopwords]
    
    # Frequencia das palavras com stopwords
    def frequence_word(self) -> list:
        frequence_words = {} # Precisa inicializar com 0
        
        for word in self.text:
            frequence_words[word] = frequence_words.setdefault(word, 0) + 1
            
        return Text.sort_tuples(list(frequence_words.items()), 1) # Ordena a lista de tuplas retornada pelo metodo .items()

    # Retorna um dicionario com a palavra como chave a sua frequencia de aparicao no texto como valor
    def frequence_word_not_stopwords(self) -> list:
        
        frequence_words = {}
        
        for word in self.extract_stopwords():
            frequence_words[word] = frequence_words.setdefault(word, 0) + 1
            
        return Text.sort_tuples(list(frequence_words.items()), 1) # Ordena a lista de tuplas retornada pelo metodo .items()
    
    # Retorna as palavras de frequencia igual a 1
    def hapax_legomenon(self):
        return [word for word, frequence in self.frequence_word_not_stopwords() if frequence == 1]
    
    # Tira os pontos do texto e retorna ja splitado nos espacos
    @staticmethod
    def extract_ponctuation(text: str) -> list[str]:
        ponctuation = ['.',',',';',':','!','?','\"',"\'","\n","\t","—"] # Adicionar mais simbolos se necessario
        list_word = text.split()
        
        for caracter in ponctuation:
            for i in range(len(list_word)):
                if caracter in list_word[i]:
                    list_word[i] = list_word[i].replace(caracter, "") # Troca os caracteres de pontuacao por espacos e substitui a string
                    
        for caracter in ponctuation:
            for i in range(len(list_word)):
                if caracter in list_word:
                    list_word.pop(i) # Troca os caracteres de pontuacao por espacos e substitui a string
                
        
        return list_word
    
    # Ordenacao usando o algoritimo quick_sort
    @staticmethod
    def sort_tuples(list_tuples: list[tuple], index_tuples_sort: int) -> list[tuple]:
        if len(list_tuples) <= 1:
            return list_tuples
        else:
            pivot = list_tuples[0] # Escolhe um pivo 

            left = [value for value in list_tuples[1:] if value[index_tuples_sort] >= pivot[index_tuples_sort]] # Lista de elementos com valor menor que o pivo
            right = [value for value in list_tuples[1:] if value[index_tuples_sort] < pivot[index_tuples_sort]]
        

            return Text.sort_tuples(left, index_tuples_sort) + [pivot] + Text.sort_tuples(right, index_tuples_sort) # Quick_sort