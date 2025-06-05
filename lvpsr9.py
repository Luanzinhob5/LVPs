def main():
    #Declarar variaveis
    entrada = str()
    saida_v = str()
    saida_c = str()

    entrada = input()
    for letra in entrada:
        if letra.upper() in "AEIOU":
            saida_v += letra
        else:
            saida_c += letra
    
    print(saida_v)
    print(saida_c)

            
if __name__ == '__main__':
    main()