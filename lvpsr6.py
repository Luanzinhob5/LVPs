def main():
    #Declarar variaveis
    entrada = str()

    entrada = input()
    for _ in range(len(entrada)):
        if _ % 2 != 0:
            print(entrada[_])

            
if __name__ == '__main__':
    main()