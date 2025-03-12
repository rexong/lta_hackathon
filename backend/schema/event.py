import typing

from backend.schema.crowdsource_event import CrowdsourceEvent
from backend.schema.image_event import ImageEvent 
from backend.schema.speed_event import SpeedEvent

class Event:
    def __init__(
        self,
        id,
        crowdsource_event: CrowdsourceEvent,
        image_event: ImageEvent = None,
        speed_event: SpeedEvent = None,
        is_unique = False,
        priority_score=-1,
        repeated_events = []
    ):
        self.id = id 
        self.crowdsource_event = crowdsource_event
        self.image_event = image_event
        self.speed_event = speed_event
        self.is_unique = is_unique 
        self.priority_score = priority_score
        self.repeated_events: typing.List[Event] = repeated_events 

    def __str__(self):
        builder = []
        if self.crowdsource_event:
            builder.append(f"From Crowdsource Event:\n{self.crowdsource_event}")
        if self.speed_event:
            builder.append(f"From Speed Reading Event:\n{self.speed_event}")
        return "\n".join(builder)

    def to_dict(self):
        return {
            "id": self.id,
            "crowdsource_event": self.crowdsource_event.to_dict(),
            "speed_event": self.speed_event.to_dict(),
            "image_event": self.image_event.to_dict(),
            "priority_score": self.priority_score,
            "is_unique": self.is_unique,
            "repeated_events": [
                event.to_dict() for event in self.repeated_events
            ]
        }

    @classmethod
    def from_dict(cls, data):
        if (id := data.get("id")) is None:
            raise ValueError("Need ID")
        if (crowdsource_event := data.get("crowdsource_event")) is None:
            raise ValueError("Need Crowdsource Event")
        crowdsource_event = data.get("crowdsource_event", None)
        if (speed_event := data.get("speed_event")) is not None:
            speed_event = SpeedEvent.from_dict(speed_event)
        if (image_event := data.get("image_event")) is not None:
            image_event = ImageEvent.from_dict(image_event)
        priority_score = data.get("priority_score", -1)
        is_unique = data.get("is_unique", False)
        if (repeated_events := data.get("repeated_events")):
            repeated_events = [Event.from_dict(event) for event in repeated_events]
        return cls(
           id,
           crowdsource_event,
           image_event,
           speed_event,
           is_unique,
           priority_score,
           repeated_events 
        )
