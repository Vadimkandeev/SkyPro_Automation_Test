from dataclasses import dataclass, field

@dataclass
class Adress:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment


class Mailing:
    def __init__(self, to, fr0m, cost, track):
        self.to = to
        self.fr0m = fr0m
        self.cost = cost
        self.track = track
        



