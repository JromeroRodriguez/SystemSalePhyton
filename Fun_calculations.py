# funciones_calcular.py

def calculate_total(sale):
    """
    Calculates the total of a sale (price * quantity)
    sale: tuple (product, price, quantity)
    """
    product, price, quantity = sale
    return price * quantity