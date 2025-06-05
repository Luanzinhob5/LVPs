def main():
    #Declarar variaveis
    entrada = str()
    normal = str()
    ao_contrario = str()

    entrada = input()

    for letra in range(len(entrada)):
        if entrada[letra] != " ":
            normal += entrada[letra]
        if entrada[-letra -1 ] != " ":
            ao_contrario += entrada[-letra - 1]

    if normal == ao_contrario:    
        print("É PALÍNDROMO")
    else:
        print("NÃO É PALÍNDROMO")

if __name__ == '__main__':
    main()