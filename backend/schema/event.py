class Event:
    def __init__(self, timestamp="", town="", street="", congestion_level="", speed="", end_node=""):
        self.timestamp = timestamp
        self.town = town
        self.street = street
        self.congestion_level = congestion_level
        self.speed = speed 
        self.end_node = end_node

    @classmethod
    def create(cls, timestamp, town, street, congestion_level, speed, end_node):
        return cls(timestamp, town, street, congestion_level, speed, end_node)
