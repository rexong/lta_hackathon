
    # Get incoming data from backend via API, but for now use dummy data
    # TODO: integrate with backend via API (two-way)
    # TODO: consider whether there is a need to display non-user-friendly info to user i.e. longitude, latitude
    if "incoming" not in st.session_state:
        st.session_state["incoming"] = []
        dummy1 = { # Data headers refer to Waze excel sent by Temo
            "id": 123,
            "longitude": 103.3,
            "latitude": 1.2,
            "road_name": "PIE", # Street name / Road name
            "date_time": "2025-03-07 10:00", # YYYY-MM-DD HH-MM
            "alert_type": "Hazard", # Hazard / Jam / Road Closed
            "alert_subtype": "Hazard on shoulder, car stopped", # Subtype
            "details": "xxxxxxxxxxx",
        }
        dummy2 = {
            "id": 105,
            "longitude": 103.5,
            "latitude": 1.4,
            "road_name": "Sengkang West Rd", # Street name / Road name
            "date_time": "2025-02-28 20:00", # YYYY-MM-DD HH-MM
            "alert_type": "Jam", # Hazard / Jam / Road Closed
            "alert_subtype": "Jam, stand-still traffic", # Subtype
            "details": "xxxxxxxxxxx",
        }
        st.session_state["incoming"].append(dummy1)
        st.session_state["incoming"].append(dummy2)

    # Data after filtering
    # Get filtered data from APi
    # TODO: get data from backend via API
    if "filtered" not in st.session_state:
        st.session_state["filtered"] = []
        dummy1 = { # Data headers refer to Waze excel sent by Temo
            "id": 201,
            "longitude": 103.88,
            "latitude": 1.36,
            "road_name": "Farrer Rd", # Street name / Road name
            "date_time": "2025-01-10 12:00", # YYYY-MM-DD HH-MM
            "alert_type": "Road Closed", # Hazard / Jam / Road Closed
            "alert_subtype": "Road Closed Event", # Subtype
            "details": "xxxxxxxxxxx",
            "priority": "High",
        }
        dummy2 = {
            "id": 153,
            "longitude": 103.84,
            "latitude": 1.32,
            "road_name": "Tiong Bahru Rd", # Street name / Road name
            "date_time": "2025-02-15 16:30", # YYYY-MM-DD HH-MM
            "alert_type": "Jam", # Hazard / Jam / Road Closed
            "alert_subtype": "Jam, heavy traffic", # Subtype
            "details": "xxxxxxxxxxx",
            "priority": "Medium",
        }
        st.session_state["filtered"].append(dummy1)
        st.session_state["filtered"].append(dummy2)