from backend.schema.event import Event
from backend.schema.event_storage import EventStorage

class VerifiedManager:
    def __init__(self):
        self.storage = EventStorage()

    def get_all(self):
        return self.storage.list_events()

    def get_one(self, event_id):
        return self.storage.read(event_id)
    
    def delete(self, event_id):
        return self.storage.delete(event_id)
    
    def add_verified_event(self, verified_event: Event):
        return self.storage.create(
            verified_event.crowdsource_event, 
            verified_event.image_event,
            verified_event.speed_event,
            verified_event.is_unique,
            verified_event.priority_score
        )

    def add_repeated_event(self, verified_event_id, repeated_event):
        event = self.storage.update(verified_event_id, repeated_event)
        return event
        
    #TODO
    def dispatch(self):
        pass