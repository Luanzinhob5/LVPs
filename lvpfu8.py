def main():
    #Declarar variaveis
    end = True

    #Funcao MDC
    def mdc(n1,n2,n3):
        end = True
        n = n3
        while end:
            if n1 % n == 0 and n2 % n == 0 and n3 % n == 0:
                mdc = n
                end = False
            else:
                n -=1

        print(f"MDC({n1}, {n2}, {n3})={mdc}")

    for _ in range(4):
        n1= int(input())
        n2= int(input())
        n3= int(input())
        mdc(n1,n2,n3)

if __name__ == '__main__':
    main()