from pyswip import Prolog
from collections import Counter

prolog = Prolog()
prolog.consult('quienesquien.pl')

def choose_question(characters):
    
    all_features = []
    
    half_characters = len(characters) / 2
    
    for p in characters:
        features = list(prolog.query(f"features({p}, F)."))
        for c in features[0]['F']:
            all_features.append(c)
    
    count_features = Counter(all_features)
    value_features = list(count_features.values())
    
    best_subset = min(value_features, key=lambda x: abs(x - half_characters))
    
    best_feature = ''
    
    for f, count in count_features.items():
        if count == best_subset:
            best_feature = f
    
    return best_feature

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
    
    features_characters = list(prolog.query(f"features({select_character_}, F)."))
    print(f"{select_character_.upper()} tiene las siguientes características: {features_characters[0]['F']}")

    features = choose_question(characters_list)
    
    print(features)

if __name__ == '__main__':
    main()