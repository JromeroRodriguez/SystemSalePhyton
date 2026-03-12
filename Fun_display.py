# funciones_mostrar.py

from Fun_calculations import calculate_total

def show_summary(sales, grand_total):
    print("\n--- SALES SUMMARY ---")
    for sale in sales:
        # Extraemos los valores del diccionario
        p = sale["product"]
        pr = sale["price"]
        q = sale["quantity"]
        total = calculate_total(sale)
        
        print(f"{p} - Price: {pr} - Quantity: {q} - Total: {total}")
    
    print(f"---")
    print(f"GRAND TOTAL OF THE DAY: {grand_total}")