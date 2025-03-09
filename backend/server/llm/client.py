import requests


BASE_URL = "http://127.0.0.1:5000/events"

def get_event(event_id, storage_type):
    response = requests.get(
        f"{BASE_URL}/{storage_type}/{event_id}",
    )
    if response.status_code == 200:
        event = response.json()
        return event 
    else: 
        return "Error: Cannot get {storage_type} event"

#------------------- Crowdsource Utils -------------------#
def get_crowdsource_event(event_id):
    return get_event(event_id, "crowdsource")

#------------------- Filtered Utils -------------------#
def get_filtered_event(event_id):
    return get_event(event_id, "filtered")

def add_filtered_event(event):
    response = requests.post(
        f"{BASE_URL}/filtered",
        json=event
    )
    if response.status_code == 201:
        return "Successfully added event", event
    return "Cannot add event", None

def update_filtered_event(event, event_id):
    response = requests.put(
        f"{BASE_URL}/filtered/{event_id}",
        json=event
    )
    if response.status_code == 200:
        return "Successfully updated event", event
    return "Cannot update event", None

#------------------- Verified Utils -------------------#
def get_verified_events():
    verified_events_response = requests.get(
        f"{BASE_URL}/verified"
    )
    if verified_events_response.status_code == 200:
        verified_events = verified_events_response.json()
        return verified_events
    else:
        return "Error: Cannot get verified events"
