import requests
from sseclient import SSEClient

URL = "http://localhost:5000"
CROWDSOURCE_URI = "store/crowdsource"
FILTERED_URI = "store/filtered"

def listen_to_sse(uri):
    try:
        response = requests.get(f'{URL}/{uri}', stream=True)
        response.raise_for_status()  
        client = SSEClient(response)
        for event in client.events():
            print(f"Received event id: {event.data}")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the backend. Please make sure the server is running.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def listen_to_crowdsource():
    listen_to_sse(CROWDSOURCE_URI)

def listen_to_filtered():
    listen_to_sse(FILTERED_URI)
    

if __name__ == "__main__":
    listen_to_sse()
