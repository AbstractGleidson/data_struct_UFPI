# 📊 Tarefa de PLN — Estrutura de Dados

Programa desenvolvido para a disciplina de **Estrutura de Dados** com professor Raimundo, com foco em alguns conceitos básicos de processamento de linguagem natural.

---

##  Funcionalidades

- 📄 Leitura de arquivos `.txt`
- 🧹 Remoção de pontuação e stopwords (palavras irrelevantes)
- 📈 Cálculo da frequência de palavras (com e sem stopwords)
- 🔍 Identificação de *hapax legomena* (palavras que aparecem apenas uma vez)
- 📊 Visualização gráfica das frequências com Matplotlib


---

## 🛠 Estrutura do Código

- **`Text.py`** — Classe principal para manipulação e análise de texto.
- **`frequency_graph.py`** — Arquivo com funções para exibir o gráfico da frequência de palavras.
- **`main.py`** — Executa o programa e integra todas as funcionalidades.

---

## 📚 Bibliotecas Utilizadas

- [**NLTK**](https://www.nltk.org/) ![NLTK](https://img.shields.io/badge/NLTK-Stopwords-blue)  
  Utilizada para remoção de stopwords.

- [**Matplotlib**](https://matplotlib.org/) ![Matplotlib](https://img.shields.io/badge/Matplotlib-Gráficos-orange)  
  Usada para criar gráfico de barras da frequências das palavras.

- [**Path**](https://docs.python.org/3/library/pathlib.html) ![Path](https://img.shields.io/badge/Path-Leitura%20de%20arquivos-green)  
  Auxilia na manipulação de caminhos de arquivos e leitura de textos.

---

## ▶️ Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/AbstractGleidson/data_struct_UFPI.git
   cd data_struct_UFPI/conceitos_basicos_PLN/src
   python main.py <caminho_do_arquivo_txt>