def main():
    end = True
    #Funcao MDC
    def mdc(n):
        end2 = True
        
        # while end2:
        #     if num < 0:
        #         end2 = False
        #     else:
        #         if num // 2 == 0:
        #             bina += "0"
        #             num /= 2
        #         elif num // 2 == 1:
        #             bina += "1"
        #             num /= 2


        print(f"DEC={n}")
        print(f"BIN={bin(n)[2:]}")
        print(f"HEX={(hex(n)[2:]).upper()}")
        
    while end:
        n = int(input())
        if n < 0:
            end = False
        else:
            mdc(n)                
        
        

   
if __name__ == '__main__':
    main()