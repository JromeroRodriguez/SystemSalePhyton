# Funciones de validaciones de entrada corregidas

def validate_text(prompt):
    value = input(prompt).strip()
    
    if not value:
        print("Error: Field cannot be empty.")
        return validate_text(prompt)
    
    if not value.replace(" ", "").isalpha():
        print("Error: Text must not contain numbers or symbols.")
        return validate_text(prompt)
        
    return value

def validate_number(prompt):
    try:
        value = float(input(prompt))
        if value <= 0:
            print("Error: Number must be greater than zero.")
            return validate_number(prompt)
        return value
    except ValueError: 
        print("Error: Invalid input. Please enter a number.")
        return validate_number(prompt)

def validate_integer(prompt):
    try:
        value = int(input(prompt))
        if value <= 0:
            print("Error: Number must be greater than zero.")
            return validate_integer(prompt)
        return value
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        return validate_integer(prompt)