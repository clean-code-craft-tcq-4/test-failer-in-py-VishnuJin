from wire_color_pairs.even_color_pairs import EvenColorPairs

major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]


def generate_color_map():
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(((i * 5 + j), major, minor))
    return color_map


def get_color_pair_from_number(pairnumber):
    color_pair = generate_color_map()[pairnumber]
    return color_pair[1:]


def format_color_map(color_pair):
    pair_number, major_color, minor_color = color_pair
    return f'{pair_number} | {major_color} | {minor_color}'


def print_color_map(color_map):
    for color_pair in color_map:
        print(format_color_map(color_pair))

assert get_color_pair_from_number(1) == ("White", "Blue")
assert format_color_map((1, 'White', 'Blue')) == "1  | White  | Blue"
assert format_color_map((20, 'Violet', 'Blue')) == "20 | Violet | Blue"


# the new implementation is just for learning from previous class
expected_color_map = EvenColorPairs()
actual_even_color_map = generate_color_map()
assert get_color_pair_from_number(1) == expected_color_map.get_color_from_pairnumber(1)

actual_format_color_map = format_color_map(actual_even_color_map)
exepected_format_color_map = expected_color_map.format_color_pair()
assert actual_format_color_map == exepected_format_color_map

print("All is well (maybe!)\n")
