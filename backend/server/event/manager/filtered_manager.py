from backend.schema.event_storage import EventStorage

from backend.server.event.manager.manager import CROWDSOURCE_MANAGER, VERIFIED_MANAGER
from backend.llm.model import FILTERER, PRIORITIZER

class FilteredManager:
    def __init__(self):
        self.storage = EventStorage()
    
    def notify(self, crowdsource_manager_event_id):
        event_from_crowdsource = CROWDSOURCE_MANAGER.get_one(crowdsource_manager_event_id)
        if self.__is_new_event(event_from_crowdsource):
            return self.__create_filtered_event(event_from_crowdsource) 
        else:
            not_filtered_event = VERIFIED_MANAGER.add_repeated_event(event_from_crowdsource)
            return not_filtered_event

    def get_all(self):
        return self.storage.list_events()

    def get_one(self, event_id):
        return self.storage.read(event_id)
    
    def delete(self, event_id):
        return self.storage.delete(event_id)
    
    def __create_filtered_event(self, event_from_crowdsource):
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
    
    def __is_new_event(self, new_crowdsource_event):
        verified_events = VERIFIED_MANAGER.get_all()
        for verified_event in verified_events:
            status, explanation = FILTERER.filter(new_crowdsource_event, verified_event)
            if status == "repeated":
                return False 
        return True
    
    def __calculate_priority_score(self, event):
        score, explanation = PRIORITIZER.prioritize(event)
        return score

        