def main():
    #Declarar variaveis
    o = 0

    for palavra in range(5):
        nome = input()
        palavras = nome.split(" ")
        for palavra in palavras:
            print(f"{palavra} tem {len(palavra)} letras")
        
   

if __name__ == '__main__':
    main()