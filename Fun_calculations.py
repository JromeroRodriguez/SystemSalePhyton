

# funciones_calcular.py

def calculate_total(sale):
    """
    Calculates the total using dictionary keys
    sale: dict {"product": str, "price": float, "quantity": int}
    """
    # Accedemos por nombre, lo que hace el código más legible
    return sale["price"] * sale["quantity"]