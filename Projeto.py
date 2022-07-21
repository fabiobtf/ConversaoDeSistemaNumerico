nun = int(input('Digite o número que você deseja converter: '))
nunTr = nun
op = int(input('''Escolha qual a base de conversão você quer usar:
[1] Binário
[2] Octal
[3] Hexadecimal
[4] Todas as Opções:'''))

if op == 1: #Decimal para Binario
    N_Conv = str(nun % 2)
    nun = int(nun / 2)
    while nun > 0:
        N_Conv = str(nun % 2) + N_Conv
        nun = int(nun / 2)
    print('O número ', nunTr, 'em Binário é igual a', N_Conv)
elif op == 2: #Decimal para octal
    N_Conv = str(nun % 8)
    nun = int(nun / 8)
    while nun > 0:
        N_Conv = str(nun % 8) + N_Conv
        nun = int(nun / 8)
    print('O número ', nunTr, 'em Octal é igual a', N_Conv)


elif op == 3: #Decimal para Hexadecimal
    N_Conv = int(nun % 16)
    if N_Conv > 9:
        a = 1
        if N_Conv == 10: N_Conv = 'A'
        if N_Conv == 11: N_Conv = 'B'
        if N_Conv == 12: N_Conv = 'C' 
        if N_Conv == 13: N_Conv = 'D'
        if N_Conv == 14: N_Conv = 'E'
        if N_Conv == 15: N_Conv = 'F'
    else:
        N_Conv = str(nun % 16)
    nun = int(nun / 16)
    while nun > 0:
        num_Add = int(nun % 16)
        if num_Add > 9:
            a = 1
            if num_Add == 10:
                num_Add = 'A'
            if num_Add == 11:
                num_Add = 'B'
            if num_Add == 12:
                num_Add = 'C'
            if num_Add == 13:
                num_Add = 'D'
            if num_Add == 14:
                num_Add = 'E'
            if num_Add == 15:
                num_Add = 'F'
        else:
            num_Add = str(nun % 16)        
        N_Conv = num_Add + N_Conv
        nun = int(nun / 16)
    print('O número', nunTr,'em Hexadecimal é igual a', N_Conv)
elif op == 4: #Aqui utilizamos as funções para mostrar que tem uma forma mais simples de elabora o codigo
    print("Todas as Opcões")
    print("{}  para Binario é igual a {}". format(nun, bin(nun)))
    print("{}  para Octal é igual a {}". format(nun, oct(nun)))
    print("{}  Orção para Hexadecimal é igual a {}". format(nun, hex(nun)))
else:
        print('Opção inválida. Tente Novamente.')
        
