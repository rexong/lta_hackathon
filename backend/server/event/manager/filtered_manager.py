import logging

logger = logging.getLogger(__name__)

from backend.schema.event_storage import EventStorage

from backend.server.event.manager.manager import CROWDSOURCE_MANAGER, VERIFIED_MANAGER
from backend.llm.model import FILTERER, PRIORITIZER

class FilteredManager:
    def __init__(self):
        logger.info("Filtered Storage: Storage Initialised")
        self.storage = EventStorage()
    
    def notify(self, crowdsource_manager_event_id):
        logger.info("Filtered Storage: Got Notified of New Crowdsource Event")
        event_from_crowdsource = CROWDSOURCE_MANAGER.get_one(crowdsource_manager_event_id)
        is_new_event, verified_event_id = self.__filter_event(event_from_crowdsource)
        if is_new_event:
            return self.__create_filtered_event(event_from_crowdsource) 
        else:
            logger.info("Filtered Storage: Informing Verified Manager to add repeated event")
            not_filtered_event = VERIFIED_MANAGER.add_repeated_event(verified_event_id, event_from_crowdsource)
            return not_filtered_event

    def get_all(self):
        logger.info("Filtered Storage: Listing all Events")
        return self.storage.list_events()

    def get_one(self, event_id):
        logger.info("Filtered Storage: Listing one event")
        return self.storage.read(event_id)
    
    def delete(self, event_id):
        logger.info("Filtered Storage: Deleting one event")
        return self.storage.delete(event_id)
    
    def __create_filtered_event(self, event_from_crowdsource):
        logger.info("Filtered Storage: Adding unique event")
        crowdsource_event = event_from_crowdsource.crowdsource_event
        image_event = event_from_crowdsource.image_event
        speed_event = event_from_crowdsource.speed_event
        priority_score = self.__calculate_priority_score(event_from_crowdsource)
        filtered_event = self.storage.create(
            crowdsource_event,
            image_event,
            speed_event,
            True,
            priority_score
        )
        return filtered_event
    
    def __filter_event(self, new_crowdsource_event):
        logger.info("Filtered Storage: Check Event is unique")
        verified_events = VERIFIED_MANAGER.get_all()
        for verified_event in verified_events:
            status, explanation = FILTERER.filter(new_crowdsource_event, verified_event)
            if status == "repeated":
                logger.info("Filtered Storage: Duplicated Event Found")
                return False, verified_event.id 
        logger.info("Filtered Storage: Unique Event Found")
        return True, -1
    
    def __calculate_priority_score(self, event):
        logger.info("Filtered Storage: Calculating Priority Score")
        score, explanation = PRIORITIZER.prioritize(event)
        return score
