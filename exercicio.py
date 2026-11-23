'''
CRIE UMA FUNÇÃO QUE MULTIPLICA TODOS OS ARGUMENTOS NÃO NOMEADOS 
RECEBIDOS RETORNE O TOTAL PARA UMA VARIÁVEL E MOSTRE O VALOR DA
VARIÁVEL
'''
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicao = multiplicar(10,6)
print(multiplicao)