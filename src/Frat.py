from classes import *
if __name__ == '__main__':
    # create all the beds
    bed_1 = Bed("bed 1", "single")
    bed_2 = Bed("bed 2", "single")
    bed_3 = Bed("bed 3", "single")
    bed_4 = Bed("bed 4", "single")
    bed_5 = Bed("bed 5", "single")

    # Create all the rooms
    room_1 = Room("room 1", [bed_1])
    room_2 = Room("room 2", [bed_2])
    room_3 = Room("room 3", [bed_3])
    room_4 = Room("room 4", [bed_4])
    room_5 = Room("room 5", [bed_5])

    # Create the house
    the_house = House(1050)

    # Add rooms to the house
    the_house.add_room(room_1)
    the_house.add_room(room_2)
    the_house.add_room(room_3)
    the_house.add_room(room_4)
    the_house.add_room(room_5)

    # Create the people and their bids
    Tim = Person("Tim")
    Tom = Person("Tom")
    Schubert = Person("Schubert")
    Jack = Person("Jack")
    Watson = Person("Watt")

    # Add bids to a person
    Tim.add_bids({
        "room 1": 20,
        "room 2": 20,
        "room 3": 40,
        "room 4": 20,
        "room 5": 20
    })
    Tom.add_bids({
        "room 1": 20,
        "room 2": 20,
        "room 3": 40,
        "room 4": 20,
        "room 5": 20
    })
    Schubert.add_bids({
        "room 1": -20,
        "room 2": 20,
        "room 3": 40,
        "room 4": 20,
        "room 5": 20
    })
    Jack.add_bids({
        "room 1": 20,
        "room 2": 20,
        "room 3": 40,
        "room 4": 20,
        "room 5": 20
    })
    Watson.add_bids({
        "room 1": 20,
        "room 2": 20,
        "room 3": 40,
        "room 4": 80,
        "room 5": 20
    })

    test = Calculator(price_by="total average", bid_value="extra")

    # Add people to the calculator
    test.add_people([Tim, Tom, Jack, Schubert, Watson])

    # Add house to calculator
    test.add_house(the_house)

    # Calculate prices
    test.calculate()
    test.view_results()
