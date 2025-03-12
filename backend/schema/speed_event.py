class SpeedEvent:
    def __init__(
        self, 
        past_week_avg_speed,
        current_avg_speed,
        x, y
    ):
        self.past_week_avg_speed = past_week_avg_speed
        self.current_avg_speed = current_avg_speed
        self.coordinate = (x, y)

    def to_dict(self):
        return {
            "past_week_avg_speed": self.past_week_avg_speed,
            "current_avg_speed": self.current_avg_speed,
            "x": self.coordinate[0], "y": self.coordinate[1]
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"""\
Coordinate: {self.coordinate}
Past Week Average Speed: {self.past_week_avg_speed}
Current Average Speed: {self.current_avg_speed}
"""
