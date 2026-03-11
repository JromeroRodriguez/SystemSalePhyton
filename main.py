# main.py

from Fun_registration import register_sales
from Fun_display import show_summary

if __name__ == "__main__":
    # Register daily sales
    sales, grand_total = register_sales()
    

    # Show sales summary
    show_summary(sales, grand_total)

print("Thank you for using the sales registration system")