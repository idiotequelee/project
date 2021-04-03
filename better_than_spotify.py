  
import json


def main():
    while True:
        welcome_message()
        user_input = input("Enter the option you would like to do in your library: \n")
        if user_input == "1":
            view_library(parse_json())
        elif user_input == "2":
            create_artist()
        elif user_input == "3":
            edit_artist()
        elif user_input == "4":
            delete_artist()
        elif user_input == "5":
            break
        else:
            print("Please, enter the options from 1 to 5")


def welcome_message():
    print("1 - view my library")
    print("2 - create new artist")
    print("3 - edit an artist in your library")
    print("4 - delete an artist")
    print("5 - exit the program")
    print("\n")


def parse_json():
    json_file = open('better_than_spotify_2.json', 'r')
    json_data = json_file.read()
    data = json.loads(json_data)
    return data


def save_json(data):
    with open('better_than_spotify_2.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)


def view_library(parse_j_func):
    data = parse_j_func
    index = 0
    for artist in data:
        band = artist['band']
        participants = artist['participants']
        albums = artist['albums']
        year = artist['year']
        print(f"Index: {index}")
        print(f"Artist: {band}")
        print(f"Participants: {participants}")
        print(f"Albums: {albums}")
        print(f"Year of establishment: {year}")
        print("\n")
        index += 1


def create_artist():
    library = parse_json()
    band = input("Enter the name of the band: ")
    participants = input("Enter the participants separated by comma: ")
    albums = input("Enter the albums separated by comma: ")
    year = int(input("Enter the year of the establishment: "))

    library.append({
        'band': band,
        'participants': participants.split(","),
        'albums': albums.split(","),
        'year': year
    })
    save_json(library)


def delete_artist():
    view_library(parse_json())
    new_library = []
    data = parse_json()
    library_size = len(data)-1
    index = 0
    delete_option = input(f"Which artist would you like to delete? \nChoose the number from 0 to {library_size}: ")
    for artist in data:
        if index == int(delete_option):
            pass
            index += 1
        else:
            new_library.append(artist)
            index += 1
    save_json(new_library)

   
def edit_artist():
    view_library(parse_json())
    new_library = []
    data = parse_json()
    library_size = len(data)-1
    index = 0
    edit_option = input(f"Which artist would you like to edit? \nChoose the number from 0 to {library_size}: ")
    for artist in data:
        if index == int(edit_option):
            band = artist['band']
            participants = artist['participants']
            albums = artist['albums']
            year = artist['year']
            print(f"Current name of artist: {band}")
            band = input("Enter new name of the band: ")
            print(f"Current participants: {participants}")
            participants = input("Enter new participants separated by comma: ")
            print(f"Current albums: {albums}")
            albums = input("Enter new albums separated by comma: ")
            print(f"Current year of establishment: {year}")
            year = int(input("Enter new year of the establishment: "))
            new_library.append({"band": band, "participants": participants, "albums": albums, "year": year})
            index += 1
        else:
            new_library.append(artist)
            index += 1
    save_json(new_library)


main()   






