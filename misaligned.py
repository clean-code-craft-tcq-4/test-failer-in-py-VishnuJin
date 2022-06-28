from wire_color_pairs.even_color_pairs import EvenColorPairs
from wire_color_pairs.color_pair import ColorPair
from exception_handlers import get_error_type


color_map = EvenColorPairs()

assert color_map.get_color_from_pairnumber(1) == ("White", "Blue")
assert (
    color_map.format_color_pair_item(ColorPair(1, "White", "Blue"))
    == " 1 |  White |   Blue"
)
assert (
    color_map.format_color_pair_item(ColorPair(20, "Yellow", "Slate"))
    == "20 | Yellow |  Slate"
)

assert get_error_type(color_map.get_color_from_pairnumber, 100) == ValueError
assert get_error_type(color_map.get_color_from_pairnumber, "A") == TypeError

print("All is well\n")
