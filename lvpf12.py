import random

def main():
    #Declarar variaveis
    
    def validador():
        contador = 10
        contagem = 0
        contagem_ultimo_numero = 0
        entrada = input()
        numeros = entrada.replace(".","").replace("-","")
        for numero in numeros:
            if contador > 1:
                contagem += int(numero) * contador
            if contador > 0:
                contagem_ultimo_numero += int(numero) * (contador + 1)
                contador -= 1

        if contagem % 11 < 2 and int(numeros[9]) != 0 or contagem_ultimo_numero % 11 < 2 and int(numeros[10]) != 0:
            print(f"CPF INVÁLIDO")
        elif (11 - (contagem_ultimo_numero % 11) != int(numeros[10]) and contagem % 11 < 2) or (11 - (contagem % 11) != int(numeros[9]) and contagem % 11 < 2):
            print(f"CPF INVÁLIDO")
        else:
            print(f"CPF VÁLIDO")
    validador()

if __name__ == '__main__':
    main()