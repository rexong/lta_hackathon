from backend.schema.event import Event

class EventStorage:
    def __init__(self):
        self.events: dict[int, Event] = {}
        self.counter = 1  

    def create(
        self, 
        timestamp,
        town, 
        street,
        x,
        y,
        alert_type,
        alert_subtype,
        reliability,
        image_src="",
        current_speed="",
        previous_speed=""
    ):
        event_id = self.counter
        event = Event.create(
            event_id,
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
            previous_speed
        )
        self.events[event_id] = event
        self.counter += 1
        return event 

    def read(self, event_id):
        return self.events.get(event_id, None)

    def update(
        self,
        event_id,
        timestamp=None,
        town=None, 
        street=None,
        x=None,
        y=None,
        alert_type=None,
        alert_subtype=None,
        reliability=None,
        image_src=None,
        current_speed=None,
        previous_speed=None,
        score=None
    ):
        event = self.events.get(event_id, None)
        if event:
            if timestamp:
                event.timestamp = timestamp
            if town:
                event.town = town
            if street:
                event.street = street
            if x:
                event.x = x
            if y:
                event.y = y
            if alert_type:
                event.alert_type = alert_type
            if alert_subtype:
                event.alert_subtype = alert_subtype
            if reliability:
                event.reliability = reliability
            if image_src:
                event.image_src = image_src
            if current_speed:
                event.current_speed = current_speed
            if previous_speed:
                event.previous_speed = previous_speed
            if score:
                event.score = score
            return event
        return None

    def delete(self, event_id):
        return self.events.pop(event_id, None)

    def list_events(self):
        return list(self.events.values())