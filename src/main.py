from typing import List, Dict


class Bed:
    """A bed in the house. Can be double or single"""

    def __init__(self, name: str, size: str):
        """A bed in the house. Can be double or single"""
        self._name = name
        self._size = size
        if self._size == "single":
            self._spaces = 1
        elif self._size == "double":
            self._spaces = 2
        else:
            raise IOError

    def get_size(self):
        """type of bed"""
        return self._size

    def get_spaces(self):
        """number of people that can sleep in this bed"""
        return self._spaces


class Room:
    """A room with beds of the same type in it"""

    def __init__(self, name: str, beds: List[Bed]):
        """Has beds in it"""
        self._name = name
        self._beds = beds

    def add_bed(self, bed: Bed):
        """Add a bed to a room"""
        self._beds.append(bed)


class Person(object):
    """A person that is going on the trip"""

    def __init__(self, name: str, gender: str, days_staying: int):
        """A person that will be there during the holiday
        :param name: Name of person
        :param gender: Gender of person ('m' or 'f')
        :param days_staying: Number of nights the person is staying
        """
        self._name = name
        self._gender = gender
        self._days_staying = days_staying
        self.partner = None
        self._bids = {}

    def get_name(self):
        """"Name of person"""
        return self._name

    def get_gender(self):
        """Gender of person"""
        return self._gender

    def days_staying(self):
        "Number of days the person is staying"
        return self._days_staying

    def get_partner(self):
        """Partner of person"""
        return self.partner

    def add_partner(self, partner):
        """Add a partner to a person"""
        self.partner : Person = partner
        partner.partner = self

    def get_bids(self):
        """The bids of this person"""
        return self._bids

    def add_bids(self, bids: Dict[str, float]):
        """Add bids to a person"""
        self._bids =


class House:
    """House with beds"""

    def __init__(self, price: float, nights: int):
        """House that you are staying in. Has beds and a price
        :param price: Total price of accomodation
        :param nights: Number of nights you are staying at accomodation
        """
        self._price = price
        self.rooms: List[Room] = []
        self.nights = nights

    def get_price(self):
        """ The price per night of the house"""
        return self._price

    def get_rooms(self):
        """The beds in the house"""
        return self.rooms

    def add_room(self, room: Room):
        """Add a bed to the house"""
        self.rooms.append(room)

    def get_nights(self):
        """Number of nights you are staying"""
        return self.nights

    def price_per_night(self):
        """Price the group is paying per night"""
        return self._price / self.nights


class Calculator(object):
    """Calculates the best permutation of bed selections"""

    def __init__(self):
        """Calculate the best permutation of bed/room assignments. And the prices that everyone has to pay for them"""
        self._house = None
        self._people: list = []
        self._highest_utility: int = None

    def get_house(self):
        """"Returns house"""
        return self._house

    def get_people(self):
        """Returns list of people in the experiment """
        return self._people

    def add_person(self, person: Person):
        """Add a person to the calculator"""
        self._people.append(person)

    def add_people(self, people: List[Person]):
        """Add a list of people to the calculator"""
        self._people.extend(people)

    def get_highest_utility(self):
        """Returns highest utility value found"""
        return self._highest_utility

    def add_house(self, house: House):
        """Add a house to the calculator"""
        self._house = house


if __name__ == '__main__':
    test = Calculator()

    # create all the beds
    bunk_1 = Bed("bunk 1", "single")
    bunk_2 = Bed("bunk 2", "single")
    bunk_3 = Bed("bunk 3", "single")
    bunk_4 = Bed("bunk 4", "single")
    bunk_5 = Bed("bunk 5", "single")
    bunk_6 = Bed("bunk 6", "single")
    single_1 = Bed("single 1", "single")
    single_2 = Bed("single 2", "single")
    queen = Bed("Queen", "double")
    king = Bed("King", "double")

    # Create all the rooms
    bunk_room = Room("bunk room", [bunk_1, bunk_2, bunk_3, bunk_4, bunk_5, bunk_6])
    twin_room = Room("twin room", [single_1, single_2])
    queen_room = Room("queen room", [queen])
    king_room = Room("king room", [king])

    # Create the house
    the_house = House(547, 3)

    # Create the people and their bids
    lewis = Person("lewis", "m", 3)
    braydon = Person("braydon", "m", 3)
    tim = Person("tim", "m", 3)
    jess = Person("jess", "f", 3)
    daniel = Person("daniel", "m", 3)
    emma = Person("emma", "f", 3)
    sam = Person("sam", "m", 3)
    mel = Person("mel", "f", 3)
    michael = Person("michael", "m", 2)
    sarah = Person("sarah", "f", 1)

    # Add rooms to the house
    the_house.add_room(bunk_room)
    the_house.add_room(twin_room)
    the_house.add_room(queen_room)
    the_house.add_room(king_room)

    # Add house to calculator
    test.add_house(the_house)

    # Add people to the calculator
    test.add_people([lewis, braydon, tim, jess, daniel, emma, sam, mel, michael, sarah])

    # Add partner to a person
    lewis.add_partner(jess)

    # Add bids to a person
    lewis.add_bids({
        "bunk room": 100,
        "twin room": 150,
        "queen room": 200,
        "king room": 200
    })

