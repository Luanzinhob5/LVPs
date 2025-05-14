def main():
    #Declarar variaveis
    imc = float(0)
    peso = float(0)
    altura = float(0)
    
    #Entrada de dados
    peso = float(input())
    altura = float(input())

    #Processos
    imc = peso / (altura**2)
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 24.9:
        print(f"Peso normal")
    elif imc < 29.9:
        print(f"Sobrepeso")
    else:
        print(f"Obesidade")
if __name__ == '__main__':
    main()