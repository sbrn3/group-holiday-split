from typing import List, Dict
from itertools import product


class Person(object):
    """A person that is going on the trip"""
    _name: str

    def __init__(self, name: str, gender: str = "hello", days_staying: int = 1):
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

    def get_nights_staying(self):
        """Number of days the person is staying"""
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

    def __init__(self, price: float, nights: int = 1):
        """House that you are staying in. Has beds and a price
        :param price: Total price of accommodation
        :param nights: Number of nights you are staying at accommodation
        """
        self._price = price
        self.rooms: List[Room] = []
        self.nights = nights

    def get_total_price(self):
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
    house: House

    def __init__(self, couple_force=False, couple_priority=False,
                 price_by: str = "individual", bid_value: str = "direct"):
        """Calculate the best permutation of bed/room assignments. And the prices that everyone has to pay for them

        :param price_by can be either 'room' or 'individual'
        :param bid_value can be either "direct" or "extra" """
        self._people: list = []
        self._highest_utility: int = 0
        self.best_arrangements: Dict[List[float]: int] = {}
        self.couple_force = couple_force
        self.couple_priority = couple_priority
        self.price_by = price_by
        self.bid_value = bid_value

    def get_house(self):
        """"Returns house"""
        return self.house

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
        self.house = house

    def get_house(self):
        """Get house that is in calculator"""
        return self.house

    def calculate(self):
        """Calculates the room assignment for every person in the house

        In the form of a dictionary which maps {person: room} """
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
                print(round(count / total, 2))
                if utility >= self._highest_utility:
                    self._highest_utility = utility
                    self.best_arrangements[str(arrangement)] = utility
        return self.filter_highest_utility()

    def filter_highest_utility(self):
        """Goes through all the potential best arrangements and only keeps the values with the highest utility"""
        max_dictionary: Dict[str: int] = {}
        max_value: float = max(self.best_arrangements.values())
        for i in self.best_arrangements.keys():
            if self.best_arrangements[i] == max_value:
                max_dictionary[i] = max_value
        self.best_arrangements = max_dictionary

    @staticmethod
    def string_to_list(n: str) -> List[int]:
        """Converts a string that used to be a list of integers, back into a list of integers"""
        n = n.replace(" ", "")
        n = n.strip("[]")
        n = n.split(",")
        n = list(map(int, n))
        return n

    def is_valid_arrangement(self, arrangement: List[int]):
        """Bool of whether the tuple is a valid arrangement for rooms"""
        rooms: List[Room] = self.house.get_rooms()
        for room in range(len(rooms)):
            # How many people were assigned to the room
            assigned_to_room = arrangement.count(room + 1)

            # Have less than 2 people been assigned to the room
            if assigned_to_room < 2:
                continue

            # More assigned than there is space
            space_in_room = rooms[room].get_capacity()
            if assigned_to_room > space_in_room:
                return False

            # Is this a gender restricted room
            if rooms[room].is_gender_restricted():
                # Find the people assigned to this room
                indexed_people: List[Person] = self.indexed_people(room + 1, arrangement)
                # Couple force
                if self.couple_force:
                    # If you have a partner
                    if indexed_people[0].get_partner() is not None:
                        if not indexed_people[0].is_couple(indexed_people[1]):
                            return False
                # Are they a couple?
                if indexed_people[0].is_couple(indexed_people[1]):
                    continue
                # Are the genders all the same
                if indexed_people[0].get_gender() != indexed_people[1].get_gender():
                    return False
            else:
                if self.couple_force:
                    # couples can only be in gender restricted rooms
                    indexed_people: List[Person] = self.indexed_people(room + 1, arrangement)
                    for person in indexed_people:
                        if person.get_partner() in indexed_people:
                            return False

        return True

    def calculate_utility(self, arrangement: List[int]):
        """Calculates the utility of a particular arrangement.

        This value is the sum of the bids for each person with each group"""
        utility_score: float = 0
        # For every person
        for person in self.get_people():
            # Find out what room they were put in
            arrangement_index: int = self.get_people().index(person)
            room_index = arrangement[arrangement_index] - 1
            room: Room = self.house.get_rooms()[room_index]
            room_name: str = room.get_name()
            # How much did they bid on that room
            bid: int = person.get_bids()[room_name]
            bid *= person.get_nights_staying()
            # Add to the total utility score
            utility_score += bid
            # If person has a partner
            if person.get_partner() is not None and self.couple_priority:
                # If the partner is in this room
                partner: Person = person.get_partner()
                partner_index = self.get_people().index(partner)
                partner_room_index = arrangement[partner_index] - 1
                partner_room: Room = self.house.get_rooms()[partner_room_index]
                if partner_room == room:
                    partner_bid = partner.get_bids()[room_name]
                    partner_bid *= partner.get_nights_staying()
                    utility_score += partner_bid
        return utility_score

    def get_room_mapping(self, arrangement: List[int]):
        """Create a dictionary mapping a person to a room"""
        if isinstance(arrangement, str):
            arrangement = self.string_to_list(arrangement)
        the_map: Dict[Person: Room] = {}
        for person_index in range(len(arrangement)):
            person: Person = self.get_people()[person_index]
            room_index: int = arrangement[person_index] - 1
            room: Room = self.house.get_rooms()[room_index]
            the_map[person] = room
        return the_map

    def room_average(self, arrangement: List[int]):
        """Calculates the average value bid of everyone in that room"""
        room_bids = []
        for i, room in enumerate(self.get_house().get_rooms()):
            index_people: List[Person] = self.indexed_people(i + 1, arrangement)
            room_total = 0
            for person in index_people:
                room_total += person.get_bids()[room.get_name()]
            room_bids.append(room_total / len(index_people))
        return room_bids

    def total_average(self):
        """Calculates the average value bid of everyone"""
        room_bids = []
        for i, room in enumerate(self.get_house().get_rooms()):
            room_total = 0
            for person in self.get_people():
                room_total += person.get_bids()[room.get_name()]
            room_bids.append(room_total / len(self.get_people()))
        return room_bids

    @staticmethod
    def median(numbers: List[float]):
        """Calculates the median of a list of numbers

        If the list is even it calculates the average of the two middle numbers"""
        if len(numbers) % 2 == 0:
            after: int = int(len(numbers) / 2)
            before: int = after - 1
            return (numbers[before] + numbers[after]) / 2
        else:
            return numbers[int((len(numbers) + 1) / 2)]

    def total_median(self):
        """Calculates the median value bid of everyone"""
        room_bids = []
        for i, room in enumerate(self.get_house().get_rooms()):
            individual_bids = []
            for person in self.get_people():
                individual_bids.append(person.get_bids()[room.get_name()])
            room_bids.append(self.median(individual_bids))
        return room_bids

    def room_median(self, arrangement: List[int]):
        """Calculates the median value bid of everyone in the same room"""
        room_bids = []
        for i, room in enumerate(self.get_house().get_rooms()):
            index_people: List[Person] = self.indexed_people(i + 1, arrangement)
            individual_bids = []
            for person in index_people:
                individual_bids.append(person.get_bids()[room.get_name()])
            room_bids.append(self.median(individual_bids))
        return room_bids

    def get_price_mapping(self, arrangement: List[int]):
        """Create a dictionary mapping a person to a price"""
        if isinstance(arrangement, str):
            arrangement = self.string_to_list(arrangement)
        the_map: Dict[Person: float] = {}
        room_bids = []
        if self.price_by == "individual":
            # Calculate by how much people actually bid directly
            room_bids = self.individual(arrangement)
        elif self.price_by == "room average":
            # Calculate the average cost per night of each room
            room_bids = self.room_average(arrangement)
        elif self.price_by == "total average":
            room_bids = self.total_average()
        elif self.price_by == "total median":
            room_bids = self.total_median()
        elif self.price_by == "room median":
            room_bids = self.room_median(arrangement)
        else:
            raise ValueError
        # Scale the room bids depending on the bid by options
        original = room_bids
        if self.bid_value == "extra":
            equal_bids = [self.house.get_total_price()/len(room_bids)] * len(room_bids)
            room_bids = [x + y for x, y in zip(equal_bids, room_bids)]
        scale = self.house.get_total_price() / sum(room_bids)
        scaled_room_bids = [i * scale for i in room_bids]
        # Dictionary matching rooms to prices
        room_prices = {}
        for i, room in enumerate(self.get_house().get_rooms()):
            room_prices[room] = scaled_room_bids[i]
        # Create dictionary matching prices to people
        for i, person in enumerate(self.get_people()):
            # What is their assigned room?
            their_room_map = self.get_room_mapping(arrangement)
            their_room = their_room_map[person]
            # What is the value of that room
            the_map[person] = round(room_prices[their_room])
        test = sum(the_map.values())
        return the_map

    def individual(self, arrangement):
        bids: List[int] = []
        # Calculate the total value of bids
        for person_index in range(len(arrangement)):
            person: Person = self.get_people()[person_index]
            room_index: int = arrangement[person_index] - 1
            room: Room = self.house.get_rooms()[room_index]
            bid = person.get_bids()[room.get_name()] * person.get_nights_staying()
            bids.append(bid)
        # Calculate individual costs
        for person_index in range(len(arrangement)):
            # Get the first person
            person: Person = self.get_people()[person_index]
            room_index: int = arrangement[person_index] - 1
            room: Room = self.house.get_rooms()[room_index]
            # What is the persons bid for their assigned room
            bid = person.get_bids()[room.get_name()] * person.get_nights_staying()
            bids[person_index] = bid
        return(bids)


    def get_best_arrangement(self):
        """Returns best arrangement"""
        return self.best_arrangements

    def calculate_arrangements(self):
        """Calculates a list of lists which map people to rooms"""
        x = list(product(range(1, len(self.house.get_rooms()) + 1), repeat=len(self.get_people())))
        return x

    def indexed_people(self, room_number: int, arrangement: List[int]) -> List[Person]:
        """People at indexes"""
        indexed_people: List[Person] = []
        # People indexed to room n
        for i in range(len(arrangement)):
            if room_number == arrangement[i]:
                indexed_people.append(self.get_people()[i])
        return indexed_people

    def view_results(self):
        """View the results of the calculation"""
        # print(self.best_arrangements)
        # print(len(self.best_arrangements))
        print("Room assignment: ")
        arrangement = list(self.best_arrangements.keys())[0]
        print(self.get_room_mapping(arrangement))
        print("Prices assigned per person: ")
        payment = self.get_price_mapping(arrangement)
        print(payment)
        print("Total amount paid per week is ${0}".format(sum(payment.values())))