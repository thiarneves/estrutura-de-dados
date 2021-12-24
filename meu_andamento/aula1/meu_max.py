from math import inf
from time import time

def meu_max(iteravel):
    numero_maximo = -inf
    for numero in iteravel:
        if numero > numero_maximo:
            numero_maximo = numero
    return numero_maximo


if __name__ == '__main__':

    print('Estudo de tempo de execução função maximo\n')

    for n in range(100, 1001,100):    
        inicio = time()
        print("Maximo é: ", meu_max(range(n)))
        fim = time()

        tempo_total = fim - inicio
        print("tempo total teste 1 = {}".format(tempo_total))



