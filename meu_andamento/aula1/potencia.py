def potencia_iterativa(base: int, expoente: int):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado


def _potencia_recursiva_linear(base, expoente, resultado=1):
    if expoente ==0:
        return resultado
    return _potencia_recursiva_linear(base, expoente -1, resultado * base)


def potencia_recursiva_linear(base: int, expoente: int):
    
    
    return _potencia_recursiva_linear(base, expoente -1, base)


if __name__ == "__main__":
    print(potencia_iterativa(2, 10))
    print(potencia_recursiva_linear(2, 10))