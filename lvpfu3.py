def main():
    #Declarar variaveis
    entrada = int(input())
    
    def numero(entrada):
        if entrada > 0:
            print("P")

        elif entrada == 0:
            print("Z")

        elif entrada < 0:
            print("N")

    numero(entrada)
    
if __name__ == '__main__':
    main()