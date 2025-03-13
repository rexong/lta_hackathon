import logging

logger = logging.getLogger(__name__)

from backend.schema.event_storage import EventStorage
from backend.schema.crowdsource_event import CrowdsourceEvent
from backend.schema.image_event import ImageEvent
from backend.schema.speed_event import SpeedEvent

class CrowdsourceManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "storage"):
            logger.info("Crowdsource Storage: Storage Initialised")
            self.storage = EventStorage()
    
    def add(
        self,
        timestamp,
        town,
        street,
        x, y,
        alert_type,
        reliability,
        alert_subtype = "" 
    ):
        logger.info("Crowdsource Storage: Add new crowdsource event")
        crowdsource_event = CrowdsourceEvent(
            timestamp, 
            town, 
            street,
            x, y, 
            alert_type, 
            reliability, 
            alert_subtype
        )
        image_event = self.__get_image_event(x, y)
        speed_event = self.__get_speed_event(x, y)
        event = self.storage.create(
            crowdsource_event,
            image_event,
            speed_event
        )
        return event

    def get_all(self):
        logger.info("Crowdsource Storage: Listing all Events")
        return self.storage.list_events()

    def get_one(self, event_id):
        logger.info("Crowdsource Storage: Listing one event")
        return self.storage.read(event_id)
    
    def delete(self, event_id):
        logger.info("Crowdsource Storage: Deleting one event")
        return self.storage.delete(event_id)
    
    #TODO
    def __get_image_event(self, x, y) -> ImageEvent:
        logger.info("Crowdsource Storage: Retrieving Images")
        return None

    #TODO
    def __get_speed_event(self, x, y) -> SpeedEvent:
        logger.info("Crowdsource Storage: Retrieving Speed")
        return None

if __name__ == "__main__":
    manager = CrowdsourceManager()

    data = {
        "timestamp": "2024-10-21 08:30:00",
        "town": "Tampines",
        "street": "Tampines Ave 10",
        "x": 103.928405,
        "y": 1.354571,
        "alert_type": "ACCIDENT",
        "reliability": 6 
    }

    event = manager.add(**data)
    retrieved_event = manager.get_one(event.id)
    print(retrieved_event)
    print(retrieved_event.to_dict())
    retrieved_events = manager.get_all()
    print(retrieved_events)
    print(retrieved_events[0])
