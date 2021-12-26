chamadas_recursivas=0

def _torre_de_hanoi_recursivo(numero_de_discos, origem, destino, auxiliar):
    global chamadas_recursivas
    chamadas_recursivas+=1
    if numero_de_discos ==1:
        print(f'{origem} -> {destino} : {numero_de_discos}')
        return
    _torre_de_hanoi_recursivo(numero_de_discos - 1, origem, auxiliar, destino)
    print(f'{origem} -> {destino} : {numero_de_discos}')
    _torre_de_hanoi_recursivo(numero_de_discos - 1, auxiliar, destino, origem)

def torre_de_hanoi(numero_de_discos: int):
    global chamadas_recursivas
    chamadas_recursivas=0
    _torre_de_hanoi_recursivo(numero_de_discos, origem='A', destino='B', auxiliar='C')
    

if __name__ == "__main__":
    for i in range(1,30):
        print(f'### Hanoi para {i} discos')
        torre_de_hanoi(i)
        print(chamadas_recursivas)
    
