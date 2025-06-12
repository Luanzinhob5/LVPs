def main():
    #Declarar variaveis
    
    def bissexto():
        entrada = int(input())

        if ((entrada % 4) == 0 and (entrada % 100) != 0 ) or ((entrada % 400) == 0):
            print("É BISSEXTO")

        else:
            print("NÃO É BISSEXTO")

    bissexto()
if __name__ == '__main__':
    main()