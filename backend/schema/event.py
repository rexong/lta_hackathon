class Event:
    def __init__(
            self,
            id="",
            timestamp="",
            town="",
            street="",
            x="",
            y="",
            alert_type="",
            alert_subtype="",
            reliability="",
            image_src="",
            current_speed="",
            previous_speed="",
            score=-1
    ):
        self.id = id 
        self.timestamp = timestamp
        self.town = town
        self.street = street
        self.x = x
        self.y = y
        self.alert_type = alert_type
        self.alert_subtype = alert_subtype
        self.reliability = reliability
        self.image_src = image_src
        self.current_speed = current_speed
        self.previous_speed = previous_speed
        self.score = score 

    def __str__(self):
        return f"""\
Time: {self.timestamp}
Town: {self.town}
Street: {self.street}
Coordinates: ({self.x}, {self.y})
Alert Type: {self.alert_type}
Alert Subtype: {self.alert_subtype}
Reliability: {self.reliability}
Current Average Speed on Street: {self.current_speed}
Past Week Average Speed on Street: {self.previous_speed}
"""

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "town": self.town, 
            "street": self.street,
            "x": self.x,
            "y": self.y,
            "alert_type": self.alert_type,
            "alert_subtype": self.alert_subtype,
            "reliability": self.reliability,
            "current_speed": self.current_speed,
            "previous_speed": self.previous_speed,
            "image_src": self.image_src,
            "score": self.score
        }

    @classmethod
    def from_dict(self, data):
        return Event.create(
            data.get("id", ""),
            data.get("timestamp", ""),
            data.get("town", ""),
            data.get("street", ""),
            data.get("x", ""),
            data.get("y", ""),
            data.get("alert_type", ""),
            data.get("alert_subtype", ""),
            data.get("reliability", ""),
            data.get("current_speed", ""),
            data.get("previous_speed", ""),
            data.get("image_src", ""),
            data.get("score", -1)
        )

    @classmethod
    def create(
        cls, 
        id="",
        timestamp="",
        town="",
        street="",
        x="",
        y="",
        alert_type="",
        alert_subtype="",
        reliability="",
        image_src="",
        current_speed="",
        previous_speed="",
        score=-1
    ):
        return cls(
            id,
            timestamp,
            town,
            street,
            x,
            y,
            alert_type,
            alert_subtype,
            reliability,
            image_src,
            current_speed,
            previous_speed,
            score
        )
