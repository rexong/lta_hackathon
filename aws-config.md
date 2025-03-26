# AWS EC2 Guide

## Accessing the Virtual Machine
To access the virtual machine, you will need the secret key file `lta_hackathon_pair.pem`. Make sure you have it save somewhere in your directory. 

Then open the terminal you prefer and go to the directory with the `lta_hackathon_pair.pem` file. Then run the following command:
> ssh -i "lta_hackathon_pair.pem" ubuntu@ec2-13-213-52-104.ap-southeast-1.compute.amazonaws.com

*When logging in for the first time, you will be prompted about some fingerprint thingy, just type `yes`.*

To confirm that you are in the VM, you should see something like `ubuntu@13.213.52.104`

## Using TMUX
Do look up some tutorials on how to use tmux.
There should be an existing tmux session active, and to connect to this session
run the following command:
> tmux attach

The existing session has 2 windows where the first window has 2 panes and second window has 1 pane. 
For simplicity sake, the first window is used to run both backend servers, one in each pane. To start both servers, run the following command:
> flask -A backend.server.app run --host=0.0.0.0 --port=5000
and 
> flask -A backend.scripts.lta_datamall.app run --host=0.0.0.0 --port=8000

To start the frontend
> streamlit run frontend.py

## Turning off
If you are down, just close your terminal. Dont have to exit tmux or exit the VM.
