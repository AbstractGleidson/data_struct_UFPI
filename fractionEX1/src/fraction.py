class Fraction:
    _numerador = 0
    _denominador = 0 
    
    # Metodo contrutor da funcao Fraction
    def __init__(self,numerador: int, denominador: int):
        self.numerador = numerador
        
        if denominador == 0:
            self.denominador = 1
            print("Valor digitado para o denominador é inválido: denominador = 1")
        else:
            self.denominador = denominador    
        
    # Metodo str sobrescritro, para mostrar a fracao "formatada"
    def __str__(self):
        return  f"({self.numerador}/{self.denominador})" if (self.numerador % self.denominador != 0) else f"{self.numerador // self.denominador}"
    
    # Retorna o Valor do denominador
    def getNumerador(self):
        return self.numerador
    
    # Retorna o valor do denominador
    def getDenominador(self):
        return self.denominador
    
    # Troca o valor do denominador
    def setDenominador(self, newDenominador: int):
        if newDenominador == 0:
            self.denominador = 1
            return 
        self.denominador = newDenominador
        
    # Troca o valor do numerador
    def setNumerador(self, newNumerador: int):
        self.numerador = newNumerador
    
    # Tira o Maior Divisor Comum de duas fracoes  
    @staticmethod    
    def MDC(numerador, denominador):
        if numerador %  denominador == 0:
            return denominador
        else:
            return Fraction.MDC(denominador, (numerador % denominador))   
    
    # Simplifica a fracao 
    def simpleFraction(self):
        valueMDC = Fraction.MDC(self.numerador, self.denominador) # Pega o maximo divisor comum da fracao
        
        self.numerador //= valueMDC # simplifica o denominador
        self.denominador //= valueMDC # simplifica o nominador
        
    # Operador de soma (+)
    def __add__(self, fraction):
        new_numerador = (self.numerador * fraction.denominador) + (fraction.numerador * self.denominador) # Novo numerador 
        new_denominador = self.denominador * fraction.denominador # Novo denominador 
        
        fraction = Fraction(new_numerador, new_denominador)
        fraction.simpleFraction() # Simplifica fracao
        
        return fraction # retorna a nova fracao
    
    # Operador de subtracao (-)
    def __sub__(self, fraction):
        new_numerador = (self.numerador * fraction.denominador) - (fraction.numerador * self.denominador) # Novo numerador 
        new_denominador = self.denominador * fraction.denominador # Novo denominador 
        
        fraction = Fraction(new_numerador, new_denominador)
        fraction.simpleFraction() # Simplifica fracao
        
        return fraction  # retorna a nova fracao
    
    # Operador de multiplicacao (*)
    def __mul__(self, fraction):
        new_numerador = (self.numerador * fraction.numerador) # Novo numerador 
        new_denominador = (self.denominador * fraction.denominador) # Novo denominador 
        
        fraction = Fraction(new_numerador, new_denominador)
        fraction.simpleFraction() # Simplifica fracao
        
        return fraction  # retorna a nova fracao
    
    # Operador de divisao (/)
    def __truediv__(self, fraction):
        new_numerador = (self.numerador * fraction.denominador) # Novo numerador 
        new_denominador = (self.denominador * fraction.numerador) # Novo denominador 
        
        fraction = Fraction(new_numerador, new_denominador)
        fraction.simpleFraction() # Simplifica fracao
        
        return fraction  # retorna a nova fracao
    
    # Operador de igualdade (==)
    def __eq__(self, fraction) -> bool:
        return (self.numerador == fraction.numerador) and (self.denominador == fraction.denominador) 
    
    # Operador de diferenca (!=) 
    def __ne__(self, fraction) -> bool:
        return (self.numerador != fraction.numerador) or (self.denominador != fraction.denominador)
    
    # Operador ralacional maior (>)
    def __gt__(self, fraction2) -> bool:
        fraction1 = Fraction(self.numerador, self.denominador) # Cria a primeira fracao
        resultFraction = fraction1 - fraction2 # Tira a diferenca dessas duas fracoes 
        
        return (resultFraction.numerador) > 0 or (resultFraction.numerador < 0 and resultFraction.denominador < 0)
    
    # Operador relacional maior igual (>=)
    def __ge__(self, fraction2) -> bool:
        fraction1 = Fraction(self.numerador, self.denominador) # Cria a primeira fracao
    
        return (fraction1 > fraction2) or (fraction1 == fraction2)
    
    # Operador relacional menor (<)
    def __lt__(self, fraction2) -> bool:
        fraction1 = Fraction(self.numerador, self.denominador)
        
        return not (fraction1 >= fraction2)
    
    # Operador relacional menor igual (<=)
    def __le__(self, fraction2) -> bool:
        fraction1 = Fraction(self.numerador, self.denominador)
        
        return not (fraction1 > fraction2)