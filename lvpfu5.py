def main():
    #Declarar variaveis
    numero = int(input())

    def inverter(n):
        if n < 0:
            n *= -1
        invertido = 0

        while n > 0:
            resto = n % 10          
            invertido = invertido * 10 + resto  
            n = n // 10 

        return invertido
    
        
    
    print(inverter(numero))
if __name__ == '__main__':
    main()