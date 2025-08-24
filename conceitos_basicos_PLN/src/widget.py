import os 
import platform

def mainMenu() -> int:
    
    option = -1
    
    while(option > 4 or option < 1):
        print("=============================")
        print("       Menu principal")
        print("=============================")
        print("1 - Frequência com stopwords")
        print("2 - Frequência sem stopwords")
        print("3 - Hapax legomenon")
        print("4 - Sair")
        print("=============================")
        option = int(input("Opção: "))
    
    return option # Opcao escolhida pelo usuario

# Limpa o terminal
def clear():
    command = "clear" if platform.platform() == "linux" else "cls"
    os.system(command)