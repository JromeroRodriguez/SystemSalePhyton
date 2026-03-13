# main.py - entry point of the program

from Fun_registration import register_sales
from Fun_display import show_summary

if __name__ == "__main__":  # guarantees code only runs when executed directly
    
    # unpacks the implicit tuple into two separate variables
    # sales receives the list of sales
    # grand_total receives the total of the day
    sales, grand_total = register_sales()
    
    show_summary(sales, grand_total)  # displays the final summary
    print("Thank you for using the sales registration system!")