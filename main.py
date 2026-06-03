
def calcular_desconto(valor, percentual):
    """
    Calcula o valor final após aplicar desconto.
    """

    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")

    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual inválido.")

    desconto = valor * (percentual / 100)
    valor_final = valor - desconto

    return round(valor_final, 2)


def calcular_imposto(valor, percentual):
    """
    Calcula imposto sobre um valor.
    """

    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")

    imposto = valor * (percentual / 100)

    return round(imposto, 2)


if __name__ == "__main__":

    valor_produto = 1000
    desconto = 15

    valor_com_desconto = calcular_desconto(valor_produto, desconto)

    imposto = calcular_imposto(valor_com_desconto, 10)

    print(f"Valor original: R$ {valor_produto}")
    print(f"Valor com desconto: R$ {valor_com_desconto}")
    print(f"Imposto calculado: R$ {imposto}")
