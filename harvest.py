############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        "Muskmelon",
        "1998",
        "green",
        True,
        True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType(
        "cas",
        "Casaba",
        "2003",
        "orange",
        False,
        False)
    cas.add_pairing("mint")
    cas.add_pairing("strawberry")
    all_melon_types.append(cas)

    cren = MelonType(
        "cren",
        "Crenshaw",
        "1996",
        "green",
        False,
        False)
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType(
        "yw",
        "Yellow Watermelon",
        "2013",
        "yellow",
        False,
        True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    print(type(melon_types))

    for melon in melon_types:
        print(f'{melon.name} pairs with {melon.pairings}')

    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_by_code = {}
    for melon in melon_types:
        if melon.code not in melon_by_code:
            melon_by_code[melon.code] = melon
    return melon_by_code

############
# Part 2   #
############

melon_typess = make_melon_types()
print_pairing_info(melon_typess)


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, code, shape_rating, color_rating, harvested_from, harvested_by):
        """Initialize a melon for harvest."""

        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
        

    def is_sellable(self, shape_rating, color_rating):
        """Checks the sellability of the melon."""

        if self.shape_rating > 5 and self.color_rating > 5:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_objects =[]

    Melon_1 = Melon(
        "yw",
        8,
        7,
        "Field_2",
        "Sheila")
    melon_objects.append(Melon_1)

    Melon_2 = Melon(
        "yw",
        3,
        4,
        "Field_2",
        "Sheila")
    melon_objects.append(Melon_2)

    Melon_3 = Melon(
        "yw",
        9,
        8,
        "Field_3",
        "Sheila")
    melon_objects.append(Melon_3)

    Melon_4 = Melon(
        "cas",
        10
        6,
        "Field_35",
        "Sheila")
    melon_objects.append(Melon_4)

    Melon_5 = Melon(
        "cren",
        8,
        9,
        "Field_35",
        "Michael")
    melon_objects.append(Melon_5)

    Melon_6 = Melon(
        "cren",
        8,
        2,
        "Field_35",
        "Michael")
    melon_objects.append(Melon_6)

    Melon_7 = Melon(
        "cren",
        2,
        3,
        "Field_4",
        "Michael")
    melon_objects.append(Melon_7)


    Melon_8 = Melon(
        "mush",
        6,
        7,
        "Field_4",
        "Michael")
    melon_objects.append(Melon_8)

    Melon_9 = Melon(
        "yw",
        7,
        10,
        "Field_3",
        "Sheila")
    melon_objects.append(Melon_9)


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
