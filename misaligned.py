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


def format_color_map(color_map):
    formatted_color_pairs = ""
    for color_pair in color_map:
        formatted_color_pairs += " | ".join([str(item) for item in color_pair]) + "\n"
    return formatted_color_pairs


def print_color_map(color_map):
    print(format_color_map(color_map))


expected_color_map = EvenColorPairs()
actual_even_color_map = generate_color_map()
assert get_color_pair_from_number(1) == expected_color_map.get_color_from_pairnumber(1)

actual_format_color_map = format_color_map(actual_even_color_map)
exepected_format_color_map = expected_color_map.format_color_pair()
assert actual_format_color_map == exepected_format_color_map

print("All is well (maybe!)\n")
