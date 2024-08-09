
try:
    print("Outer try")
    # Simulación de un posible error de índice
    my_list = [1, 2, 3]
    print(my_list[3])  # Esto producirá una excepción IndexError
except IndexError:
    print("Outer except: IndexError")
    try:
        print("Inner try")
        result = 4 / 0  # Esto producirá una excepción ZeroDivisionError
    except ZeroDivisionError:
        print("Inner except: ZeroDivisionError")
    except Exception as e:
        print("Inner except: General Exception", str(e))
except Exception as e:
    print("Outer except: General Exception", str(e))
