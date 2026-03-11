# Sales System Python by: Joseph Romero

Welcome to **Sales System Python**! This is a modular project designed to manage daily sales records efficiently, securely, and in an organized manner. 

##  Description
This system allows users to register multiple sales while validating every data input to prevent common errors. At the end, it generates a detailed summary including the total per product and the grand total for the day.


<img width="716" height="810" alt="di" src="https://github.com/user-attachments/assets/173ad217-175e-48fe-91ae-00b0fda19b88" />


##  Key Features
* **Robust Validation**: Filters empty inputs, negative numbers, and incorrect data types.
* **Modular Architecture**: Code is split into specific functions to make maintenance easier.
* **User-Friendly Interface**: Clear messages and an easy-to-read sales summary.

##  Project Structure

```text
Sales_System_Project/
├──  Fun_validaciones.py  # Security filters for text and numbers
├──  Fun_calculations.py  # Mathematical logic for totals
├──  Fun_inputs.py        # Captures raw user input
├──  Fun_registration.py  # Manages the sales loop and accumulation
├──  Fun_display.py       # Formats and displays results
├──  main.py               # Application entry point
└──  README.md            # Project documentation
