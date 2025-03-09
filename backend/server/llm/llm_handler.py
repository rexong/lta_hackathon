from flask import jsonify

from backend.llm.filter_crowdsource import CrowdsourceFilter
from backend.llm.prioritizer import Prioritizer
from backend.llm.model import client
from backend.schema.event import Event
from backend.server.llm.client import (
    get_verified_events,
    add_filtered_event,
    get_crowdsource_event,
    get_filtered_event,
    update_filtered_event
)

_filter_model = CrowdsourceFilter(client)
_prioritize_model = Prioritizer(client)

# Todo: Update repeated event with the lastest information
def filter_event(event_id):
    new_event = get_crowdsource_event(event_id)
    new_event = Event.from_dict(**new_event)

    verified_events = get_verified_events()
    
    for event in verified_events:
        verified_event = Event.from_dict(**event)
        status, explanation = _filter_model.filter(new_event, verified_event)
        if status == "repeated":
           return jsonify({"message": status, "explanation": explanation})
    
    message, ret = add_filtered_event(new_event.to_dict()) 
    if not ret:
        status_code = 400
    else:
        status_code = 200
    return jsonify({"message": message, "event": ret}), status_code
    
def prioritize_event(event_id):
    new_event = get_filtered_event(event_id)
    new_event = Event.from_dict(**new_event)

    score, explanation = _prioritize_model.prioritize(new_event)
    new_event.score = score
    message, ret = update_filtered_event(new_event.to_dict(), event_id)
    if not ret:
        status_code = 400
    else:
        status_code = 200
    return jsonify({"message": message, "event": ret, "explanation": explanation}), status_code





