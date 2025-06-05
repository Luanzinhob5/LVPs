def main():
    #Declarar variaveis

    entrada = input()
    if entrada == entrada[::-1]:
        print(f"{entrada} É UM PALÍNDROMO")
    else:
        print(f"{entrada} NÃO É UM PALÍNDROMO")

if __name__ == '__main__':
    main()