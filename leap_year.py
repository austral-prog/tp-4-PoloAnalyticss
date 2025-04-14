year = int(input("Ingrese un año: "))
def leap_year():
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
leap_year()
