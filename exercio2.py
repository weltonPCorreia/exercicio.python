'''
crie uma função fala se um número é par ou ímpar .
retorne se o numero é par ou ímpar
'''

def par_impar(numero):
    par = numero %2 == 0

    if par:
        return f'{numero} é par'
    else:
        return f'{numero} é impar'



print(par_impar(5))