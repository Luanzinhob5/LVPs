def main():
    #entrada de dados
    string1 = input()
    string2 = input()

    #processo do for
    if len(string1) == len(string2) and string1 == string2:
        print("MESMO TAMANHO CONTEÚDO IGUAL")
    elif len(string1) == len(string2):
        print("MESMO TAMANHO CONTEÚDO DIFERENTE")

    else:
        print("TAMANHO DIFERENTE CONTEÚDO DIFERENTE")
    

if __name__ == '__main__':
    main()