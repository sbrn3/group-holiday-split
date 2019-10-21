from typing import List, Dict
from itertools import product


class Person(object):
    """A person that is going on the trip"""
    _name: str

    def __init__(self, name: str, gender: str, days_staying: int):
        """A person that will be there during the holiday
        :type name: str
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
        self.partner: Person = partner
        partner.partner = self

    def get_bids(self):
        """The bids of this person"""
        return self._bids

    def add_bids(self, bids: Dict[str, float]):
        """Add bids to a person"""
        self._bids = bids

    def is_couple(self, other_person):
        """Is the other person, this person's partner.

        Are they a couple? """
        if self.get_partner() == other_person:
            return True
        else:
            return False

    def __repr__(self):
        return self._name


class Bed:
    """A bed in the house. Can be double or single"""

    def __init__(self, name: str, size: str):
        """A bed in the house. Can be double or single"""
        self._name: str = name
        self._size: str = size
        if self._size == "single":
            self._spaces: int = 1
        elif self._size == "double":
            self._spaces: int = 2
        else:
            raise IOError

    def get_type(self):
        """type of bed"""
        return self._size

    def get_spaces(self):
        """number of people that can sleep in this bed"""
        return self._spaces

    def __repr__(self):
        return self._name


class Room:
    """A room with beds of the same type in it"""

    def __init__(self, name: str, beds: List[Bed]):
        """Has beds in it"""
        self._name = name
        self._beds = beds
        self.capacity: int = self.calculate_capacity()
        self.people: List[Person] = []

    def add_bed(self, bed: Bed):
        """Add a bed to a room"""
        self._beds.append(bed)

    def calculate_capacity(self):
        total = 0
        for i in self._beds:
            total += i.get_spaces()
        return total

    def get_capacity(self):
        """Gets the number of people that can sleep in this room"""
        return self.capacity

    def add_person(self, person: Person) -> bool:
        """Add a person to the room.

        Will return false if the room is already full or there is no bed for someone of their gender in the room"""
        # If there is space in the room
        if self.get_capacity() <= len(self.get_people()):
            return False
        # If the bed is a double
        if self._beds[0].get_type() == "double":
            other_person = self.people[0]
            if other_person.get_gender() != person.get_gender() and other_person.get_partner() != person:
                return False
        elif len(self.get_people()) < self.get_capacity():
            self.people.append(person)
            return True
        else:
            raise IOError

    def get_people(self):
        """The people in the room"""
        return self.people

    def is_gender_restricted(self):
        """Whether this room is gender restricted

        Essentially whether it has a double bed or not"""
        for bed in self._beds:
            if bed.get_type() == "double":
                return True
        return False

    def get_name(self):
        """Name of the room"""
        return self._name

    def __repr__(self):
        return self._name


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
    _house: House

    def __init__(self):
        """Calculate the best permutation of bed/room assignments. And the prices that everyone has to pay for them"""
        self._people: list = []
        self._highest_utility: int = 0
        self.best_arrangements: List[List[int]] = []

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

    def calculate(self):
        """Calculates the room assignment for every person in the house

        In the form of a dictionary which maps {person: room} """
        answer: Dict[Person: Room] = {}

        # Get a list of all possible ways people could be put in rooms
        possible_arrangements: List[tuple] = self.calculate_arrangements()

        count = 0
        total = len(possible_arrangements)
        # Calculate the utility of every arrangement
        for arrangement in possible_arrangements:
            count += 1
            arrangement = list(arrangement)
            if self.is_valid_arrangement(arrangement):
                utility = self.calculate_utility(arrangement)
                print(round(count/total, 2))
                if utility >= self._highest_utility:
                    self._highest_utility = utility
                    self.best_arrangements.append(arrangement)

    def get_best_arrangement(self):
        """Returns best arrangement"""
        return self.best_arrangements

    def calculate_arrangements(self):
        """Calculates a list of lists which map people to rooms"""
        x = list(product(range(1, len(self._house.get_rooms()) + 1), repeat=len(self.get_people())))
        return x

    def indexed_people(self, n: int, arrangement: List[int]) -> List[Person]:
        """People at indexes"""
        indexes: List[int] = []
        # People indexed to room n
        for i in range(len(arrangement)):
            if n == arrangement[i]:
                indexes.append(i)
        indexed_people: List[Person] = []
        for i in indexes:
            indexed_people.append(self.get_people()[i])
        return indexed_people

    def is_valid_arrangement(self, room_indexes: List[int]):
        """Bool of whether the tuple is a valid arrangement for rooms"""
        rooms: List[Room] = self._house.get_rooms()
        for room in range(len(rooms)):
            # Are any of the rooms too full
            assigned_to_room = room_indexes.count(room + 1)
            space_in_room = rooms[room].get_capacity()
            if assigned_to_room > space_in_room:
                return False

            # Have less than 2 people been assigned to the room
            if assigned_to_room < 2:
                continue
            # Is this a gender restricted room
            if rooms[room].is_gender_restricted():
                # Find the people assigned to this room
                indexed_people = self.indexed_people(room + 1, room_indexes)

                # Are they a couple?
                if indexed_people[0].is_couple(indexed_people[1]):
                    continue

                # Are the genders all the same
                if indexed_people[0].get_gender() != indexed_people[1].get_gender():
                    return False
        return True

    def calculate_utility(self, arrangement: List[int]):
        utility_score: float = 0
        # For every person
        for person in self.get_people():
            # Find out what room they were put in
            arrangement_index: int = self.get_people().index(person)
            room_index = arrangement[arrangement_index] - 1
            room: Room = self._house.get_rooms()[room_index]
            room_name: str = room.get_name()
            # How much did they bid on that room
            bid: int = person.get_bids()[room_name]
            bid *= person.days_staying()
            # Add to the total utility score
            utility_score += bid
        return utility_score