import logging

logger = logging.getLogger(__name__)

from backend.schema.event_storage import EventStorage
from backend.schema.crowdsource_event import CrowdsourceEvent
from backend.schema.image_event import ImageEvent
from backend.schema.speed_event import SpeedEvent

class CrowdsourceManager:
    def __init__(self):
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
