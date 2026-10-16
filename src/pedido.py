def calcular_total_pedido(subtotal, distancia_km, cliente_vip=False):
    """Calcula o total com desconto VIP e frete, arredondado a centavos."""

    if subtotal < 0 or distancia_km < 0:
        raise ValueError("Subtotal e distância não podem ser negativos")

    desconto = subtotal * 0.10 if cliente_vip else 0
    subtotal_com_desconto = subtotal - desconto

    if subtotal_com_desconto >= 100:
        frete = 0
    else:
        frete = 8 + 1.5 * distancia_km

    total = subtotal_com_desconto + frete
    return round(float(total), 2)
