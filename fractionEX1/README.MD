# Operações com Frações: "Atividade de Aquecimento"

Este programa permite realizar diversas operações matemáticas e comparações entre **frações** no terminal, utilizando a classe `Fraction`. Esse programa é referente a primeira atividade da matéria de **estrutura de dados**.

O programa exibe um menu interativo para que o usuário escolha a operação desejada e insira duas frações.

---

## 📋 Funcionalidades

* **Soma** de frações
* **Subtração** de frações
* **Multiplicação** de frações
* **Divisão** de frações
* **Verificação de igualdade** (`==`)
* **Verificação de diferença** (`!=`)
* **Comparação se a primeira é maior** (`>`)
* **Comparação se a primeira é menor** (`<`)
* **Comparação se é maior ou igual** (`>=`)
* **Comparação se é menor ou igual** (`<=`)

---

## 🛠 Estrutura do Código

O programa é dividido em 3 arquivos principais:

1. **`main.py`** – Executa o loop principal e controla a lógica do menu.
2. **`fraction.py`** - Contém a classe responsável pelas frações e operações com as fracões, `Fraction`. 
2. **`widgets.py`** – Contém funções de input de informações pelo terminal:

   * `mainMenu()` → exibe o menu e retorna a opção escolhida.
   * `inputFraction()` → recebe a entrada de valores para a fração `numerador/denominador` e retorna uma instância da classe `Fraction`.


---

## ▶ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone o repositório:

   ```bash
   git clone https://github.com/AbstractGleidson/data_struct_UFPI.git
   cd fractionEX1/src
   ```
3. Execute o programa:

   ```bash
   python main.py
   ```

---