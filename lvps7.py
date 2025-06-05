def main():
    #Declarar variaveis
    entrada = str()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    espaco = 0

    entrada = input()

    for _ in entrada.lower():
        if _ == " ":
            espaco += 1

        elif _ == "a":
            a += 1

        elif _ == "e":
            e += 1

        elif _ == "i":
            i += 1

        elif _ == "o":
            o += 1

        elif _ == "u":
            u += 1

    print(f"ESPAÇOS EM BRANCO = {espaco}")
    print(f"A = {a}")
    print(f"E = {e}")
    print(f"I = {i}")
    print(f"O = {o}")
    print(f"U = {u}")


                
if __name__ == '__main__':
    main()