# Set up
1. Create a virtual environment
> python -m venv .venv
2. Install dependencies
> pip install -r requirements.txt
3. Make a `.env` and put the OPENAI API KEY in it

# Backend
There are 2 servers to run,

1. External Datasource - This is the mock server to LTA DataMall
2. Our own backend - This is where we handle the `crowdsource`, `filtered` and `verified` events.

To run the server, run in this order.
1. Start the External Datasource server,
> python -m backend.scripts.lta_datamall.app
2. Start our own backend
> python -m backend.server.app

You will be able to access the External Datasource at `http://localhost:8000` and our own backend at `http://localhost:5000`.

## Run Simulation
For now, we will be simulating our data. 
Ensure that both of the servers are running, then run:
> python backend/scripts/crowdsource_simulation.py 

This simulation simulates the crowdsource data that we are getting from apps like `waze`. 

## Server Sent Event
This is crucial for the frontend.
This ensure that everytime a new event is added, the frontend will be notified. There is a demo of how the frontend can utilise this Server Sent Event in `backend/client.py`.

To test out `backend/client.py`,
1. Run both servers 
2. Run
> python backend/client.py
3. Then run the simulation. 


