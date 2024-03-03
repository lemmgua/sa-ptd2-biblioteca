from rich import print
from rich.panel import Panel
from rich.table import Table
from helper import clean, press_to_confirm
from db_helper import query, insert, delete, update, custom_query
import datetime

if __name__ == "__main__":
    user_input = ""

    while user_input != "-1":
        clean()
        prompt = """[white]¡Bienvenido! Seleccione el apartado a gestionar:\n[1] Socios\n[2] Libros\n[3] Préstamos"""
        print(Panel(prompt, title="Biblio", title_align="left", style="#00FFF7 bold"))
        user_input = input()

        if user_input == "1": #Socios
            user_input_1 = ""
            while user_input_1 != "0":
                clean()
                prompt="[white]¿Qué desea hacer?\n[1] Buscar socios\n[2] Agregar socios\n[3] Editar socios\n[4] Eliminar Socios\n[0] Volver"
                print(Panel(prompt, title="Gestionar socios", title_align="left", style="#00FFF7 bold"))
                user_input_1 = input("> ")

                if user_input_1 == "1": #Buscar Socios
                    clean()
                    print("[white bold]Introduzca las columnas deseas (en blanco para todas):")
                    columns = input("> ")
                    if columns =="":
                        columns = "Nombre, DNI"
                    print("[white bold]Introduzca a continuación el criterio de búsqueda (en blanco para todos los resultados):")
                    search_query = input("> ")
                    results_table = Table()
                    [results_table.add_column(i, style="white bold") for i in columns.split(", ")]
                    [results_table.add_row(*i) for i in query(columns, "Socios", search_query)]
                    clean()
                    print(results_table)
                    press_to_confirm()

                elif user_input_1 == "2": #Agregar Socios
                    clean()
                    print("[white bold] Inserta los valores separados por comas y espacios en el siguiente formato (Nombre, DNI):")
                    values = tuple(input("> ").split(", "))
                    insert("Socios", values)
                    print("[green bold]Valores insertados correctamente")
                    press_to_confirm()
                elif user_input_1 == "3": #Editar socios
                    clean()
                    print("[white bold]Inserta las condiciones de los registros a editar:")
                    conditions_edit = input("> ")
                    print("[white bold]Inserta los valores a editar:")
                    values = input("> ")
                    update("Socios", values, conditions_edit)
                    print("[green bold]Valores editados correctamente")
                    press_to_confirm()

                elif user_input_1 == "4": #Eliminar Socios
                    clean()
                    print("[white bold]Inserta las condiciones de los registros a eliminar\n[red bold]ADVERTENCIA: se eliminar todos los valores que coincidan")
                    delete_query = input("> ")
                    delete("Socios", delete_query)
                    print("[green bold]Valores eliminados correctamente")
                    press_to_confirm()

                elif user_input_1 == "0":
                    break
                else:
                    print("[bold red]Opción incorrecta")
                    press_to_confirm()

        elif user_input == "2": #Libros
            user_input_2 = ""
            while user_input_2 != "0":
                clean()
                prompt = "[white]¿Qué desea hacer?\n[1] Buscar ejemplares\n[2] Agregar ejemplares\n[3] Eliminar ejemplares\n[0] Volver"
                print(Panel(prompt, title="Libros", title_align="left", style="#00FFF7 bold"))
                user_input_2 = input()
                if user_input_2 == "1": #Buscar
                    clean()
                    print("[white bold]Introduzca el criterio de búsqueda:")
                    search_query = input("> ")
                    results_table = Table()
                    [results_table.add_column(i, style="white bold") for i in "ISBN, Nombre, Autor".split(", ")]
                    [results_table.add_row(*i) for i in query("*", "Libros", search_query)]
                    clean()
                    print(results_table)
                    press_to_confirm()
                elif user_input_2 == "2": #Agregar
                    clean()
                    print("[white]Introduzca los valores en el siguiente formato (ISBN, Nombre, Autor)")
                    values = input("> ")
                    insert("Libros", tuple(values.split(", ")))
                    print("[green bold]Valores insertados correctamente")
                    press_to_confirm()
        elif user_input == "3": #Prestamos
            user_input_3 = ""
            while user_input_3 != "0":
                clean()
                prompt = "[white]¿Qué desea hacer?\n[2] Ver libros en prestamos\n[3] Ver socios con prestamos\n[4] Sacar libro\n[5] Devolver libro\n[0] Volver"
                print(Panel(prompt, title="Préstamos", title_align="left", style="#00FFF7 bold"))
                user_input_3 = input()
                if user_input_3 == "1": #Ver prestamos
                    results = query("*", "Prestamos")
                    results_table = Table()
                    results_table.add_column("ISBN")
                    results_table.add_column("DNI")
                    results_table.add_column("Fecha Salida")
                    results_table.add_column("Fecha Devolución")
                    [results_table.add_row(*i) for i in results]
                    print(results_table)
                    press_to_confirm()
                elif user_input_3 == "2": #Ver libros
                    clean()
                    search_query = "SELECT Libros.ISBN, Nombre, Autor FROM Libros INNER JOIN Prestamos ON Libros.ISBN = Prestamos.ISBN"
                    results = custom_query(search_query)
                    results_table = Table()
                    results_table.add_column("ISBN")
                    results_table.add_column("Nombre")
                    results_table.add_column("Autor")
                    [results_table.add_row(*i) for i in results]
                    print(results_table)
                    press_to_confirm()
                elif user_input_3 == "3": #Ver socios
                    clean()
                    search_query = "SELECT Socios.DNI, Nombre FROM Socios INNER JOIN Prestamos ON Socios.DNI = Prestamos.DNI_socio"
                    results = custom_query(search_query)
                    print(results)
                    results_table = Table()
                    results_table.add_column("DNI")
                    results_table.add_column("Nombre")
                    [results_table.add_row(*i) for i in results]
                    print(results_table)
                    press_to_confirm()

                elif user_input_3 == "4": #Sacar libro
                    clean()
                    print("[white]Introduzca los valores del préstamo (ISBN, DNI del socio):")
                    values = input("> ").split(", ")
                    values.append(str(datetime.date.today()))
                    values.append("NULL")
                    insert("Prestamos", tuple(values))
                    print("[green bold]Préstamo abierto correctamente")
                    press_to_confirm()
                    

        elif user_input == "-1":
            continue
        else:
            print("Opción incorrecta")

    clean()
    print("[bold red]Programa Terminado")
    press_to_confirm()