from backend.schema.event import Event
from backend.schema.crowdsource_event import CrowdsourceEvent
from backend.schema.image_event import ImageEvent
from backend.schema.speed_event import SpeedEvent

class EventStorage:
    def __init__(self):
        self.events: dict[int, Event] = {}
        self.counter = 1  

    def create(
        self, 
        crowdsource_event: CrowdsourceEvent,
    ):
        event_id = self.counter
        event = Event(event_id, crowdsource_event)
        self.events[event_id] = event
        self.counter += 1
        return event 

    def read(self, event_id):
        return self.events.get(event_id, None)

    def update(
        self,
        event_id,
        image_event: ImageEvent = None,
        speed_event: SpeedEvent = None,
        is_unique = False,
        priority_score = -1,
        repeated_event: Event = None
    ):
        event = self.events.get(event_id, None)
        if event:
            if image_event:
                event.image_event = image_event
            if speed_event:
                event.speed_event = speed_event
            if is_unique:
                event.is_unique = is_unique
            if priority_score:
                event.priority_score = priority_score
            if repeated_event:
                event.repeated_events.append(repeated_event)
            return event
        return None

    def delete(self, event_id):
        return self.events.pop(event_id, None)

    def list_events(self):
        return list(self.events.values())