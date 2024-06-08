from pyswip import Prolog

prolog = Prolog()
prolog.consult('quienesquien.pl')

def show_board(characters):
    
    characters_list = characters.copy()
    
    print("---------------------------------------------------------------")
    
    for i in range(3):
        for j in range(8):
            print(characters_list.pop(0), end="\t")
        print("\n")
        
    print("---------------------------------------------------------------")

def select_character():
    
    print("*Quién es quién*")
    
    board = list(prolog.query("lift_board(Board)."))
    
    characters_list = board[0]['Board']
    
    show_board(characters_list)
    
    while True:
    
        select_character = input("Selecciona a un personaje: ").strip().lower()
        
        if select_character not in characters_list:
            print(f"{select_character} no está en el tablero o está mal escrito")
        else:
            break
    
    return select_character, characters_list
    
    
def main():
    
    select_character_, characters_list = select_character()
    print(select_character_)

if __name__ == '__main__':
    main()