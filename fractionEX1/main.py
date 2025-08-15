from fraction import Fraction 

if __name__ == "__main__":
    
    fraction1 = Fraction(
        int(input("Digite o Numerador da 1° fração: ")), 
        int(input("Digite o denominador da 1° fração: "))
        ) # Instanciando um objeto do tipo Fraction
    
    fraction2 = Fraction(
        int(input("Digite o Numerador da 2° fração: ")), 
        int(input("Digite o denominador da 2° fração: "))
        ) # Instanciando um objeto do tipo Fraction
    
    fractionSum = fraction1 + fraction2 # Soma as fracoes
    fractionSub = fraction1 - fraction2 # Subtrai as fracoes 
    fractionMulti = fraction1 * fraction2 # Multiplica as fracoes
    fractionDiv = fraction1 / fraction2 # Divide as fracoes
    
    # Operadores Aritimeticos 
    print(fractionSum) 
    print(fractionSub)
    print(fractionMulti)
    print(fractionDiv)
    
    # Operadores relacionais
    print(f"São iguais? {fraction1 == fraction2}")
    print(f"São diferentes? {fraction1 != fraction2}")
    print(f"É maior? {fraction1 > fraction2}")
    print(f"É menor? {fraction1 < fraction2}")
    print(f"É maior igual? {fraction1 >= fraction2}")
    print(f"É menor igual? {fraction1 <= fraction2}")