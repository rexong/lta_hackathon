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

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "town": self.town, 
            "street": self.street,
            "congestion_level": self.congestion_level,
            "speed": self.speed,
            "end_node": self.end_node
        }

    def from_dict(self, data):
        return Event.create(
            data.get("timestamp", ""),
            data.get("town", ""),
            data.get("street", ""),
            data.get("congestion_level", ""),
            data.get("speed", ""),
            data.get("end_node", ""),
        )

    @classmethod
    def create(cls, timestamp, town, street, congestion_level, speed, end_node):
        return cls(timestamp, town, street, congestion_level, speed, end_node)
