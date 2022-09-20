# def leiaint(msg):
#     while True:
#         try:
#             a = int(input(f'{msg}'))
#         except:
#             print (f'\033[1;31mERRO! Digite um numero inteiro válido\033[m')
#         else:
#             return a
#             break
#
#
# a = leiaint('Digite um numero: ')
# print (f'Você acabou de digitar o numero {a}')

def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31mERRO! Digite um numero inteiro válido\033[m')
        if ok:
            break
    return valor


n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')