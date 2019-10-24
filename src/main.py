from classes import *
if __name__ == '__main__':
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
    the_house = House(1638, 3)

    # Add rooms to the house
    the_house.add_room(king_room)
    the_house.add_room(queen_room)
    the_house.add_room(twin_room)
    the_house.add_room(bunk_room)

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
    kaelyn = Person("kaelyn", "f", 3)
    # nathan = Person("nathan", "m", 1)
    georgia = Person("georgia", "f", 2)

    # Add people to the calculator
    # test.add_people([lewis, braydon, tim, jess, daniel, emma, sam, mel, michael, sarah])

    # Add partner to a person
    kaelyn.add_partner(jess)
    lewis.add_partner(georgia)

    # Add bids to a person
    lewis.add_bids({
        "bunk room": 20,
        "twin room": 20,
        "queen room": 40,
        "king room": 20
    })
    braydon.add_bids({
        "bunk room": 22,
        "twin room": 24.5,
        "queen room": 26,
        "king room": 27.5
    })
    tim.add_bids({
        "bunk room": 100,
        "twin room": 0,
        "queen room": 0,
        "king room": 0
    })
    jess.add_bids({
        "bunk room": 10,
        "twin room": 10,
        "queen room": 30,
        "king room": 50
    })
    daniel.add_bids({
        "bunk room": 10,
        "twin room": 30,
        "queen room": 30,
        "king room": 30
    })
    emma.add_bids({
        "bunk room": 10,
        "twin room": 20,
        "queen room": 30,
        "king room": 40
    })
    sam.add_bids({
        "bunk room": 10,
        "twin room": 30,
        "queen room": 25,
        "king room": 35
    })
    mel.add_bids({
        "bunk room": 25,
        "twin room": 25,
        "queen room": 25,
        "king room": 25
    })
    michael.add_bids({
        "bunk room": 1,
        "twin room": 9,
        "queen room": 45,
        "king room": 45
    })
    sarah.add_bids({
        "bunk room": 10,
        "twin room": 40,
        "queen room": 30,
        "king room": 20
    })
    kaelyn.add_bids({
        "bunk room": 10,
        "twin room": 10,
        "queen room": 30,
        "king room": 50
    })
    # nathan.add_bids({
    #     "bunk room": 0,
    #     "twin room": 30,
    #     "queen room": 20,
    #     "king room": 50
    # })
    georgia.add_bids({
        "bunk room": 20,
        "twin room": 20,
        "queen room": 40,
        "king room": 20
    })

    test = Calculator(couple_force=False, couple_priority=True, price_by="total average")

    # Add people to the calculator
    test.add_people([lewis, braydon, tim, jess, daniel, emma, sam, mel, michael, sarah, kaelyn, georgia])

    # Add house to calculator
    test.add_house(the_house)

    test.calculate()
    print(test.best_arrangements)
    print(len(test.best_arrangements))
    # arrangement = '[2, 4, 4, 1, 3, 4, 3, 4, 4, 4, 1, 2]'
    arrangement = test.best_arrangements.keys()[0]
    print(test.get_room_mapping(arrangement))
    payment = test.get_price_mapping(arrangement)
    print(payment)
    # aim = 1639
    print(sum(payment.values()))
