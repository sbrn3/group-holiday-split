from typing import List


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

    def __init__(self, beds: List[Bed]):
        """Has beds in it"""
        self._beds = beds

    def add_bed(self, bed: Bed):
        """Add a bed to a room"""
        self._beds.append(bed)


class Person(object):
    """A person that is going on the trip"""

    def __init__(self, name: str, gender: str, days_staying: int):
        """A person that will be there during the holiday"""
        self._name = name
        self._gender = gender
        self._days_staying = days_staying
        self._partner = None
        self._bids = {}

    def get_name(self):
        "Name of person"
        return self._name

    def get_gender(self):
        """Gender of person"""
        return self._gender

    def days_staying(self):
        "Number of days the person is staying"
        return self._days_staying

    def get_partner(self):
        """Partner of person"""
        return self._partner

    def add_partner(self, partner):
        """Add a partner to a person"""
        self._partner = partner

    def get_bids(self):
        """The bids of this person"""
        return self._bids


class House:
    """House with beds"""

    def __init__(self, price: int):
        """House that you are staying in. Has beds and a price"""
        self._price = price
        self.rooms: List[Room] = []

    def get_price(self):
        """ The price per night of the house"""
        return self._price

    def get_rooms(self):
        """The beds in the house"""
        return self.rooms

    def add_room(self, room: Room):
        """Add a bed to the house"""
        self.rooms.append(room)


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

    def get_highest_utility(self):
        """Returns highest utility value found"""
        return self._highest_utility

    def add_house(self, house: House):
        """Add a house to the calculator"""
        self._house = house


if __name__ == '__main__':
    test = Calculator()

    # create all the beds
