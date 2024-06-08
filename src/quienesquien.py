from pyswip import Prolog
from collections import Counter

prolog = Prolog()
prolog.consult('quienesquien.pl')

def  objective(characters_list, select_character_):
    if len(characters_list) == 1 and select_character_ == characters_list[0]:
        return False
    return True

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

def update_characters(characters, selected_feature, response):
    
    remaining_characters = []
    
    if response == 'si':
        
        for character in characters:
            features = list(prolog.query(f"features({character}, F)."))
            if selected_feature in features[0]['F']:
                remaining_characters.append(character)
        
    elif response == 'no':
        
        for character in characters:
            features = list(prolog.query(f"features({character}, F)."))
            if selected_feature not in features[0]['F']:
                remaining_characters.append(character)
    
    return remaining_characters

def show_board(characters):
    
    characters_list = characters.copy()
    
    print("---------------------------------------------------------------")
    
    for i in range(3):
        for j in range(8):
            if characters_list:
                print(characters_list.pop(0), end="\t")
            else:
                print("-", end="\t")
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
    
    rounds = 0
    
    while objective(characters_list, select_character_):
        
        print()
    
        features_characters = list(prolog.query(f"features({select_character_}, F)."))
        
        print(f"{select_character_.upper()} tiene las siguientes características: {features_characters[0]['F']}")

        selected_feature = choose_question(characters_list)
        
        response = input(f"Tu personajes tiene {selected_feature} [si/no]: ").strip().lower()
        
        characters_list = update_characters(characters_list, selected_feature, response)
        
        show_board(characters_list)
        
        rounds +=1
        
    print()
    print(f"Tu personaje es {(characters_list[0]).upper()}")
    print(f"Rondas: {rounds}")

if __name__ == '__main__':
    main()