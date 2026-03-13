# Calculation functions - centralized here because it is used in two modules

def calculate_total(sale):
    """
    Calculates the total using dictionary keys
    sale: dict {"product": str, "price": float, "quantity": int}
    """
    price = float(sale["price"])      # accesses price from dictionary and converts to float
    quantity = int(sale["quantity"])  # accesses quantity from dictionary and converts to int
    
    return price * quantity  # returns sale total without printing or modifying anything external