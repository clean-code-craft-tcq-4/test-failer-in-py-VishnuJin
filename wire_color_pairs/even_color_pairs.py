from functools import reduce
from wire_color_pairs.color_pair import ColorPair


class EvenColorPairs:
    def __init__(self):
        self.MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]
        self.MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
        self.even_colors = self.generate_color_pairs()

    def generate_color_pairs(self):
        even_colors = []
        for pair_number, color_pair in enumerate(
            [
                (major_color, minor_color)
                for major_color in self.MAJOR_COLORS
                for minor_color in self.MINOR_COLORS
            ]
        ):
            color_pair = ColorPair(pair_number + 1, color_pair[0], color_pair[1])
            even_colors.append(color_pair)
        return even_colors

    def get_color_from_pairnumber(self, pair_number):
        for item in self.even_colors:
            if item.pair_number == pair_number:
                return (item.major_color, item.minor_color)
        raise ValueError(f"Given PairNumber is {pair_number} Invalid")

    def format_color_pair(self):
        formatted_color_pair = ""
        ljust_pair_number = len(str(len(self.even_colors)))
        ljust_major_color = len(
            reduce(lambda x, y: x if len(x) > len(y) else y, self.MAJOR_COLORS)
        )

        ljust_minor_color = len(
            reduce(lambda x, y: x if len(x) > len(y) else y, self.MINOR_COLORS)
        )
        for color_pair_item in self.even_colors:
            pair_number = color_pair_item.pair_number
            major_color = color_pair_item.major_color
            minor_color = color_pair_item.minor_color

            formatted_color_pair += f"{pair_number:>{ljust_pair_number}} | {major_color:>{ljust_major_color}} | {minor_color:>{ljust_minor_color}}\n"
        return formatted_color_pair

    def print_color_map(self):
        print(self.format_color_pair())
