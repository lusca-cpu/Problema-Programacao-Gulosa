def erasing_and_winning (tam_num, dig):
    if 1 <= dig < tam_num <= 10**5:
        strNum = str(input("Digite o número: "))

        # tranformando a string de números em uma lista de números inteiros
        listNum = [int(num) for num in strNum]

        # eliminando o menor número possível
        if len(strNum) == tam_num:
            i=0
            while dig>0 and i<len(listNum) - 1:
                if listNum[i] < listNum[i + 1]: # verifica se o número atual é menor que o proximo, se sim ele já é eliminado 
                    listNum.pop(i)  
                    dig -= 1
                    if i > 0:
                        i -= 1
                else:
                    i += 1

            # tranformando a lista de números intieros em uma string
            num = ''.join(map(str, listNum))

            return num
        
        else:
            return False

    else:
        return False

tam_num = int(input("Digite o tamanho do número: "))
dig = int(input("Digite quantos dígitos deseja apagar: "))

guloso = erasing_and_winning(tam_num, dig)

if guloso:
    print(f'O maior número possivel é {guloso}.')
else:
    print("Não foi possivel calcular.")
