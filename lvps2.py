def main():
    #Declaracao de variaveis 
    a = int(-1)
    string_final = ""
    #entrada de dados
    string1 = input()
    #processo do for
    for i in string1:
        string_final += string1[a]
        a -=1
    print(string_final)
if __name__ == '__main__':
    main()

