# Display functions - separated because showing data is a different responsibility than registering it

from Fun_calculations import calculate_total

def show_summary(sales, grand_total):
    print("\nDAILY SALES SUMMARY")
    print("---------------------------")
    for sale in sales:  # iterates over each dictionary in the sales list
        product = sale["product"]    # extracts product name by key
        price = sale["price"]        # extracts unit price by key
        quantity = sale["quantity"]  # extracts quantity sold by key
        total = calculate_total(sale)  # calculates subtotal for this product

        print(f"Product: {product}")
        print(f"Unit price: ${price:,.0f}")    # :,.0f formats number with thousands separator
        print(f"Quantity sold: {quantity}")
        print(f"Product total: ${total:,.0f}") # :,.0f formats number with thousands separator
        print("---------------------------")

    print(f"GRAND TOTAL OF THE DAY: ${grand_total:,.0f}")  # formatted grand total