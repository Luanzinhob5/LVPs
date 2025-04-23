def main():
    #Declarar variaveis
    preco_kwh = float(0)
    n_consumidor = int(0)
    qtde_kwh = float(0)
    codigo = str()
    residencial = float(0)
    comercial = float(0)
    industrial = float(0)
    maior_consumo = float(0)
    menor_consumo = float(50000)
    numero = 0
    total = float(0)
    stop = True

    #Entrada de dado
    preco_kwh = float(input())
    while stop:
        n_consumidor = int(input())
        if n_consumidor == 0:
            stop = False
        else:
            qtde_kwh = float(input())
            codigo = str(input())
            numero += 1

            if qtde_kwh > maior_consumo:
                maior_consumo = qtde_kwh
            if qtde_kwh < menor_consumo:
                menor_consumo = qtde_kwh

            if codigo == "R":
                residencial += qtde_kwh
            elif codigo == "C":
                comercial += qtde_kwh
            else:
                industrial += qtde_kwh
            
            total += qtde_kwh
            

            print(f"{n_consumidor} {qtde_kwh * preco_kwh:.2f}")
    print(f"{maior_consumo:.2f}")
    print(f"{menor_consumo:.2f}")
    print(f"{residencial:.2f}")
    print(f"{comercial:.2f}")
    print(f"{industrial:.2f}")
    print(f"{total/numero:.2f}")


    

if __name__ == '__main__':
    main()