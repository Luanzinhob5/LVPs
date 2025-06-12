def main():
    #Declarar variaveis
    palavra_final = ''

    for palavra in range(10):
        primeira_palavra = input()
        segunda_palavra = input()
        palavra_final = primeira_palavra[:3] + segunda_palavra[-3:]
        print(palavra_final)


if __name__ == '__main__':
    main()