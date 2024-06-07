from pyswip import Prolog

prolog = Prolog()
prolog.consult('quienesquien.pl')

def contar_caracteristicas(personajes):
    pass

def mostrar_tablero(personajes):
    
    listado_personajes = personajes.copy()
    
    for i in range(3):
        for j in range(8):
            print(listado_personajes.pop(0), end="\t")
        print("\n")

def selecciona_personaje():
    
    print("*Quién es quién*")
    
    print("---------------------------------------------------------------")
    
    tablero = list(prolog.query("levantar_tablero(Tablero)."))
    
    lista_personajes = tablero[0]['Tablero']
    
    mostrar_tablero(lista_personajes)
    
    print("---------------------------------------------------------------")
    
    while True:
    
        personaje_seleccionado = input("Selecciona a un personaje: ").strip().lower()
        
        if personaje_seleccionado not in lista_personajes:
            print(f"{personaje_seleccionado} no está en el tablero o está mal escrito")
        else:
            break
    
    caracteristicas = list(prolog.query(f"caracteristicas({personaje_seleccionado}, C)."))
    
    print(f"{personaje_seleccionado} tiene las siguientes características: {caracteristicas[0]['C']}")
    
    return personaje_seleccionado
    
    
def main():
    personaje_seleccionado = selecciona_personaje()

if __name__ == '__main__':
    main()