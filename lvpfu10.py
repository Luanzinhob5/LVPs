import math

def main():
    end = True
    #Funcao capicua
    def capicua(n):
        raiz = math.isqrt(n) 

        if str(n)[::-1] == str(n) and n > 10 and raiz * raiz == n:
            print(f"{n} É CAPICUA E QUADRADO PERFEITO")
            
        elif str(n)[::-1] == str(n) and n > 10:
            print(f"{n} É CAPICUA")

        elif raiz * raiz == n:
            print(f"{n} É QUADRADO PERFEITO")
             

    while end:
        entrada = int(input())
        if entrada == "":
            end = False
        else:
            capicua(entrada)
    
if __name__ == '__main__':
    main()