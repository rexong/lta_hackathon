import requests
from sseclient import SSEClient

URL = "http://localhost:5000"
CROWDSOURCE_URI = "store/crowdsource"
FILTERED_URI = "store/filtered"

def listen_to_sse():
    response = requests.get(f'{URL}/{CROWDSOURCE_URI}', stream=True)
    client = SSEClient(response)
    for event in client.events():
        print(f"Received event id: {event.data}")

if __name__ == "__main__":
    listen_to_sse()
