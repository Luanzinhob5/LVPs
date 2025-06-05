def main():
    #Declarar variaveis
    entrada = str()
    a = -1

    entrada = input()
    for letra in entrada:
        a += 1
        if letra == "A":
            print(a)
            
if __name__ == '__main__':
    main()