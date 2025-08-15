from fraction import Fraction
import os 
import platform

class Widgets:
    
    # Menu principal de opcoes 
    @staticmethod
    def mainMenu() -> int:
        
        option = -1 # Inicializa opcao
        
        while(option < 0 or option > 10):
            print("\n=== Menu de Operações ===")
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Verificar igualdade (==)")
            print("6 - Verificar diferença (!=)")
            print("7 - Verificar se a primeira é maior (>)")
            print("8 - Verificar se a primeira é menor (<)")
            print("9 - Verificar se a primeira é maior ou igual (>=)")
            print("10 - Verificar se a primeira é menor ou igual (<=)")
            print("0 - Sair")
            
            try:
                option = int(input("Escolha uma opção: ")) # opcao escolhida
            except ValueError:
                print("Você digitou algo que não é um número!")
                option = -1 # retorna para o menu 

        Widgets.clear()
        return option
    
    # Limpa tela 
    @staticmethod
    def clear():
        command = "clear" if platform.platform() == "Linux" else "cls"
        os.system(command)
        
    # Cria uma Fracao
    @staticmethod
    def inputFraction() -> Fraction:
        
        error = True # Verifica a ocorrencia de erros 
        # Recebe valores validos para a fracao
        while(error):
            try:
                # Recebe os valores para a fracao
                numerador = int(input("Digite o numerador da fração: "))
                denominador = int(input("Digite o denominador da fração: "))
                
                # Retorna a fracao se os valores forem validos 
                fraction = Fraction(numerador=numerador, denominador=denominador)
                error = False 
            except:
                print("Valor inválido!")
                error = True 
        
        Widgets.clear()
        return fraction # Retorna fracao