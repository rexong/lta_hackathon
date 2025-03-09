class Event:
    def __init__(self, timestamp="", town="", street="", congestion_level="", speed="", end_node=""):
        self.timestamp = timestamp
        self.town = town
        self.street = street
        self.congestion_level = congestion_level
        self.speed = speed 
        self.end_node = end_node

    def __str__(self):
        return f"""\
Time: {self.timestamp}
Town: {self.town}
Street: {self.street}
End Node: {self.end_node}
Congestion Level: {self.congestion_level}
Speed: {self.speed}\
"""

    @classmethod
    def create(cls, timestamp, town, street, congestion_level, speed, end_node):
        return cls(timestamp, town, street, congestion_level, speed, end_node)
