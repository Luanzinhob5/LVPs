def main():
    #Declarar variaveis
    entrada = int(input())
    
    def calculo(a):
        saida = int(0)
        if a > 0:
            while a > 0:
                a //= 10
                saida += 1
        else:
            while a != -1:
                a //= 10
                saida += 1
        print(saida)
        
    calculo(entrada)
    

if __name__ == '__main__':
    main()