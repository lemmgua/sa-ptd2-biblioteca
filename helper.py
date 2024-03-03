from os import system, name
from rich import print

def refined_row(Data: tuple):
    data = list(Data)
    if isinstance(data[1], int) == False:
                data[1] = f"'{data[1]}'"
    return f"'{data[0]}' = {data[1]}"

def dict_to_query(Data: dict):
    query = ""

    for i in (items:=list(Data.items())):
        #Un único elemento a actualizar
        #Ej: ('carlos' = 'si', 'juan' = 50)
        if len(items) == 1:
            #Ej: ('carlos' = 'si')
            return refined_row(tuple(items[0]))
        query += refined_row(i) + ", "
    
    return "("+query[:-2]+")"

def clean():
     system('cls' if name == 'nt' else 'clear')

def press_to_confirm():
     print("[bold italic white]Presiona ENTER para continuar", end="")
     input()
     clean()

if __name__ == "__main__":
    print(dict_to_query({"carlos":"50", "juan":50}))
    print(dict_to_query({"juan":50}))
