import what3words
import itertools


geocoder = what3words.Geocoder("0VLI427Z")

def generate_combinations(words):
    combinations = list(itertools.combinations(words, 3))
    return combinations


def tuple_to_string(tup):
    string = '.'.join(map(str, tup))
    return string

def export_to_text(output_text, filename):
    with open(filename, 'a') as file:
        file.write(output_text)

# Example usage:
filename = "officalCoordinates.txt"

word_list = ["Washed", "Frost", "Robot", "Misfits", "Shady", "Goat", "Rocked", "Skull", "Lives", "Handy", "Chest", "Dawn", "Turkey", "Diet", "Parrot", "Chickens", "Locker", "Cannonball"]
combinations = generate_combinations(word_list)

# Print the combinations
for combination in combinations:
    string = tuple_to_string(combination)
    convert_to_coordinates = geocoder.convert_to_coordinates(string)
    if 'error' in convert_to_coordinates: # An error has been returned from the API
        code = convert_to_coordinates['error']['code']
    else:
        rowText = "{}: {}, {}\n".format(
            string, 
            convert_to_coordinates['coordinates']['lat'], 
            convert_to_coordinates['coordinates']['lng'])
        export_to_text(rowText,filename)

# words = "shady.shiny.joust"

# convert_to_coordinates = geocoder.convert_to_coordinates(words)
# if 'error' in convert_to_coordinates: # An error has been returned from the API
#     code = convert_to_coordinates['error']['code']
#     message = convert_to_coordinates['error']['message']
#     print (code, message)
