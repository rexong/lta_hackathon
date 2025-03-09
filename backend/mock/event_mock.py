import requests
import os
import json

# The base URL of the Flask app (make sure your app is running on http://127.0.0.1:5000/)
base_url = "http://127.0.0.1:5000/events/crowdsource"
current_dir = os.path.dirname(os.path.abspath(__file__))

events_data=[]
# Data for 5 events, with additional attributes
with open(f"{current_dir}/event_mock.json") as f:
    events_data = json.load(f)

if not events_data:
    print("Events data not found!")

# Loop through the events data and send a POST request for each
for event_data in events_data:
    response = requests.post(base_url, json=event_data)
    
    if response.status_code == 201:
        print(f"Event created successfully: {json.dumps(event_data)}")
    else:
        print(f"Failed to create event: {response.status_code}, {response.text}")

new_event_data = {
    "timestamp": "2025-04-09T14:00:00Z",
    "town": "Town20",
    "street": "Street20",
    "congestion_level": 3,
    "speed": 140.1,
    "end_node": "NodeB"
}

update_url = f"{base_url}/1"
update_response = requests.put(update_url, json=new_event_data)

if update_response.status_code == 200:
    print(f"Event updated successfully: {json.dumps(new_event_data)}")
else:
    print(f"Failed to update event: {update_response.status_code}, {update_response.text}")
