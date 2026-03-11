# funciones_mostrar.py
from Fun_calculations import calculate_total

def show_summary(sales, grand_total):
    """
    Displays all sales with their totals and the grand total.
    """
    print("\n--- SALES SUMMARY ---")
    for sale in sales:
        product, price, quantity = sale
        total = calculate_total(sale)
        print(f"{product} - Price: {price} - Quantity: {quantity} - Total: {total}")
    print(f"GRAND TOTAL OF THE DAY: {grand_total}")