from fraction import Fraction 
from widgets import Widgets

if __name__ == "__main__":
    option = -1
    
    while (option != 0):
        # Recebe a operacao a ser realizada
        option = Widgets.mainMenu()

        if(option != 0):
            fraction1 = Widgets.inputFraction() # Recebe a primeria fracao
            fraction2 = Widgets.inputFraction() # Recebe a segunda fracao
            
            # Soma
            if option == 1:
                print(f"{fraction1} + {fraction2} = {(fraction1 + fraction2)}")
            
            # Subtracao
            elif option == 2:
                print(f"{fraction1} - {fraction2} = {(fraction1 - fraction2)}")
            
            # Multiplicacao
            elif option == 3:
                print(f"{fraction1} x {fraction2} = {(fraction1 * fraction2)}")
            
            # Divisao
            elif option == 4:
                print(f"{fraction1} / {fraction2} = {(fraction1 / fraction2)}")
            
            # Igualdade 
            elif option == 5:
                print(f"{fraction1} == {fraction2} ? {(fraction1 == fraction2)}")   
            
            # Diferenca
            elif option == 6:
                print(f"{fraction1} != {fraction2} ? {(fraction1 != fraction2)}")   
                
            # Maior
            elif option == 7:
                print(f"{fraction1} > {fraction2} ? {(fraction1 > fraction2)}")
                
            # Menor
            elif option == 8:
                print(f"{fraction1} < {fraction2} ? {(fraction1 < fraction2)}")
                
            # Maior igual 
            elif option == 9:
                print(f"{fraction1} >= {fraction2} ? {(fraction1 >= fraction2)}")
            
            # Menor igual
            else:
                print(f"{fraction1} <= {fraction2} ? {(fraction1 <= fraction2)}")