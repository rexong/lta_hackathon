from backend.schema.event import Event

class EventStorage:
    def __init__(self):
        self.events: dict[int, Event] = {}
        self.counter = 1  # To generate unique event IDs

    # CREATE operation: Add a new event
    def create(
            self, 
            timestamp,
            town, 
            street,
            congestion_level,
            speed,
            end_node
        ):
        event_id = self.counter
        self.events[event_id] = event
        self.counter += 1
        event = Event.create(
            id,
            timestamp,
            town,
            street,
            congestion_level,
            speed,
            end_node
        )
        return event_id

    # READ operation: Get an event by ID
    def read(self, event_id):
        return self.events.get(event_id, None)

    # UPDATE operation: Update an event by ID
    def update(
            self,
            event_id,
            timestamp=None,
            town=None, 
            street=None,
            congestion_level=None,
            speed=None,
            end_node=None
        ):
        event = self.events.get(event_id, None)
        if event:
            if timestamp:
                event.timestamp = timestamp
            if town:
                event.town = town
            if street:
                event.street = street
            if congestion_level:
                event.congestion_level = congestion_level
            if speed:
                event.speed = speed
            if end_node:
                event.end_node = end_node
            return event
        return None

    # DELETE operation: Remove an event by ID
    def delete(self, event_id):
        return self.events.pop(event_id, None)

    # LIST all events (optional)
    def list_events(self):
        return list(self.events.values())