import pandas as pd
import pydeck as pdk
import streamlit as st
import requests

# TODO: dispatches an incident
def dispatch(incident):
    pass


# Load CSS
def load_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:  # Force UTF-8 encoding
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    # Enable full width mode
    st.set_page_config(layout="wide")

    load_css("styles.css") # Load CSS

    # Get incoming data from backend via API, but for now use dummy data
    # This data will later on be sent to backend via API to be filtered, when the user clicks on Filter button 
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

    # Data after validating 
    # Get data tagged with priority from API
    # TODO: get data from backend via API
    if "validated" not in st.session_state:
        st.session_state["validated"] = []
        dummy1 = { # Data headers refer to Waze excel sent by Temo
            "id": 108,
            "longitude": 103.8600,
            "latitude": 1.3521,
            "road_name": "PIE", # Street name / Road name
            "date_time": "2025-03-07 10:00", # YYYY-MM-DD HH-MM
            "alert_type": "Hazard", # Hazard / Jam / Road Closed
            "alert_subtype": "Hazard on shoulder, car stopped", # Subtype
            "details": "xxxxxxxxxxx",
            "priority": "High",
            "status": "❌ Undispatched",
        }
        dummy2 = {
            "id": 95,
            "longitude": 103.8600,
            "latitude": 1.3000,
            "road_name": "Sengkang West Rd", # Street name / Road name
            "date_time": "2025-02-28 20:00", # YYYY-MM-DD HH-MM
            "alert_type": "Jam", # Hazard / Jam / Road Closed
            "alert_subtype": "Jam, stand-still traffic", # Subtype
            "details": "xxxxxxxxxxx",
            "priority": "Low",
            "status": "❌ Undispatched"
        }
        st.session_state["validated"].append(dummy1)
        st.session_state["validated"].append(dummy2)

    # Data to be sent to backend to be filtered when user clicks on filter button in Table 1
    #if "incoming_to_filter" not in st.session_state:
        #st.session_state["incoming_to_filter"] = []

    # Incident to show details for upon checking of checkbox by user in Table 2
    if "selected_filtered" not in st.session_state:
        st.session_state["selected_filtered"] = None

    # Data to be sent to backend to be assigned priority when user clicks on Approve button
    # TODO: send data to backend via API
    #if "filtered_to_priority" not in st.session_state:
        #st.session_state["filtered_to_priority"] = []

    # Incident to show details for upon viewing details in Table 3
    if "selected_validated" not in st.session_state:
        st.session_state["selected_validated"] = None

    # Incident to dispatch information to Telegram etc. for
    if "incident_to_dispatch" not in st.session_state:
        st.session_state["incident_to_dispatch"] = None


    # If there are incoming incidents to be filtered i.e. user clicks filter button when there are incoming incidents
    # TODO: send data to backend
    #if st.session_state["incoming_to_filter"]:
        #pass


    # If user wants to view details of a filtered incident i.e. a checkbox is checked
    if st.session_state["selected_filtered"]:
        incident = st.session_state["filtered"][st.session_state["selected_filtered"] - 1] # Retrieve specific incident checked. Minus one to account for overcounting due to the row of column headers being included
        
        st.title("📌Incident Details")
        st.subheader("S/N xx")
        st.write(f"**Road Name:** {incident['road_name']}")
        st.write(f"**Date & Time:** {incident['date_time']}")
        st.write(f"**Incident Type:** {incident['alert_type']}")
        st.write(f"**Incident Subtype:** {incident['alert_subtype']}")
        st.write(f"**Details:** {incident['details']}")

        col1, col2, col3 = st.columns([1, 1, 1,]) # Initialise 3 columns
        if col1.button("✅ Approve"): # If incident approved, then add to incidents to be given priority assignment
            incident["status"] = "❌ Undispatched" # Add default undispatched status
            st.session_state["validated"].append(incident)
            st.session_state["filtered"].remove(incident)
            st.session_state["selected_filtered"] = None
            st.rerun()
            
        if col2.button("❌ Reject"): # If incident approved, then remove incident
            st.session_state["filtered"].remove(incident)
            st.session_state["selected_filtered"] = None
            st.rerun()

        if col3.button("⬅ Back"): # If no action taken and user presses back, go back to homepage
            st.session_state["selected_filtered"] = None
            st.rerun()

    # If user wants to view details of a validated incident i.e. a checkbox is checked
    elif st.session_state["selected_validated"]:
        incident = st.session_state["validated"][st.session_state["selected_validated"] - 1]

        st.title(f"📌S/N {incident["id"]}")

        # Inject CSS for table styling
        st.markdown("""
            <style>
                .incident-table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                    font-size: 18px;
                    text-align: left;
                }
                .incident-table th, .incident-table td {
                    padding: 12px;
                    border-bottom: 1px solid #ddd;
                }
                .incident-table th {
                    background-color: #004488;
                    color: white;
                    font-weight: bold;
                }
                .incident-table tr:hover {
                    background-color: #f1f1f1;
                }
                .incident-table td:first-child {
                    font-weight: bold;
                }
            </style>
        """, unsafe_allow_html=True)

        # Display the table using HTML inside `st.markdown()`
        st.markdown(f"""
            <table class="incident-table">
                <tr>
                    <th>Field</th>
                    <th>Information</th>
                </tr>
                <tr>
                    <td>🚗 Road Name</td>
                    <td>{incident["road_name"]}</td>
                </tr>
                <tr>
                    <td>⏰ Date & Time</td>
                    <td>{incident["date_time"]}</td>
                </tr>
                <tr>
                    <td>⚠️ Incident Type</td>
                    <td>{incident["alert_type"]}</td>
                </tr>
                <tr>
                    <td>📌 Incident Subtype</td>
                    <td>{incident["alert_subtype"]}</td>
                </tr>
                <tr>
                    <td>📝 Details</td>
                    <td>{incident["details"]}</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

        # TODO:
        # If incident is undispatched  
        if incident["status"] == "❌ Undispatched":
            col1, col2 = st.columns([1, 1,]) # Initialise 2 columns
            if col1.button("✅ Dispatch"): # If incident dispatched
                st.session_state["validated"][st.session_state["selected_validated"] - 1]["status"] = "✅ Dispatched"
                st.session_state["selected_validated"] = None
                st.rerun()

            if col2.button("⬅ Back"): # If no action taken and user presses back, go back to homepage
                st.session_state["selected_validated"] = None
                st.rerun()

        # If incident already dispatched, then remove dispatch button
        else:
            if st.button("⬅ Back"):
                st.session_state["selected_validated"] = None
                st.rerun()  


    # If user wants to dispatch information for a specific incident
    # TODO: API call to Telegram or sth
    elif st.session_state["incident_to_dispatch"]:
        pass


    # If user does nothing i.e. view homescreen
    else:
        st.title("🚦Traffic Incident Validator")

        # Different coloured cell depending on priority level
        def highlight_priority(priority):
            if priority == "High":
                return "background-color: red; color: black;"
            elif priority == "Medium":
                return "background-color: orange; color: black;"
            elif priority == "Low":
                return "background-color: yellow; color: black;"

        # Working tab (filtered and validated incidents) and Archived tab (incoming incidents)
        # TODO: style tabs
        working, archived = st.tabs(["Working Incidents", "Archived Incidents"])


        # Filtered and Validated Incidents
        with working:

            ##### Map #####
            # Display filtered and validated incidents

            # Get colour of incident
            def get_colour(incident):
                if incident["type"] == "Filtered":
                    if incident["priority"] == "High": # Return opaque red
                        return [255, 0, 0, 255]
                    elif incident["priority"] == "Medium":
                        return [255, 165, 0, 255] # Return opaque orange
                    else:
                        return [255, 255, 0, 255] # Return opaque yellow

                elif incident["type"] == "Validated":
                    opacity = 50
                    if incident["priority"] == "High": # Return transluscent red
                        return [255, 0, 0, opacity]
                    elif incident["priority"] == "Medium":
                        return [255, 165, 0, opacity] # Return transluscent orange
                    else:
                        return [255, 255, 0, opacity] # Return transluscent yellow


            # Filtered incidents layer
            data = pd.DataFrame(st.session_state["filtered"])
            data["type"] = "Filtered" # Add a type column with "Filtered" as every value in that column

            data["colour"] = data.apply(get_colour, axis=1) # Add colour column based on the incident

            filtered_layer = pdk.Layer(
                "ScatterplotLayer",
                data,
                get_position=["longitude", "latitude"],
                get_color = "colour",
                get_radius=200,
                pickable=True,
            )

            # Validated incidents layer
            # Create map markers with colour and radius
            data = pd.DataFrame(st.session_state["validated"])
            data["type"] = "Validated" # Add a type column with "Filtered" as every value in that column

            data["colour"] = data.apply(get_colour, axis=1) # Add colour columnn based on the incident
            
            validated_layer = pdk.Layer(
                "ScatterplotLayer", # Type of layer (scatterplot = markers)
                data, # Data source
                get_position=["longitude", "latitude"],
                get_color="colour", # Red colour with transparency
                get_radius=200, # Marker size
                pickable=True, # Enable hovering to show tooltips
            )

            # Define tooltip
            # TODO: different tooltip colours for different priorities?
            tooltip = {
                "html": "<b>Incident Subtype: {alert_subtype}", # Show alert subtype info
                "style": {"color": "white", "backgroundColor": "black", "padding": "5px"} # Appearance of tooltip
            }

            # Controls where the map is centered, i.e. centered around Singapore
            view_state = pdk.ViewState(
                latitude=1.3521,
                longitude=103.8198,
                zoom=11, # Zoom level
                min_zoom=10.5,
                pitch=0, # No tilt
            )

            # Renders map
            st.pydeck_chart(pdk.Deck(
                layers=[filtered_layer, validated_layer],
                initial_view_state=view_state,
                map_style="mapbox://styles/mapbox/dark-v11", # Streetview selected TODO: choose a map style that makes it easier to see the coloured dots
                tooltip=tooltip,
            ))


            #######################################
            ##### Table 2: Filtered Incidents #####
            st.header("🔍 Filtered Incidents")

            # Initialise column headers and empty row
            table_col = ["ID", "Longitude", "Latitude", "Road Name", "Date & Time", "Incident Type", "Incident Subtype", "Details", "Priority"]
            empty = ["...", "...", "...", "...", "...", "...", "...", "...", "..."]


            # If no filtered incidents, display empty table
            if not st.session_state["filtered"]:
                df = pd.DataFrame([empty],columns=table_col)
                df["S/N"] = ["🚨 No Records Found"] # Initialise serial number value as default value
                df = df[["S/N"] + table_col] # Reorder columns
                st.data_editor(df, use_container_width=True, key="filtered_incidents_editor", disabled=["S/N"] + table_col, hide_index=True)

            else:
                df = pd.DataFrame(st.session_state["filtered"])
                df.columns = table_col # Rename columns  
                df.index = range(1, len(df) + 1) # Initialise serial number column to be one-indexed
            
                df.index.name = "S/N" # Rename index column 
                df = df.drop(columns=["Details"]) # Remove "Details" column  

                # Create new column for checkbox to view details
                # TODO: checkbox vs dropdown (dropdown can include other options e.g. view, approve, reject, etc.)
                df["View Details"] = [False] * len(df)

                styled_df = df.style.applymap(highlight_priority, subset=["Priority"]) # Apply colour

                edited_df = st.data_editor(styled_df, use_container_width=True, key="filtered_incidents_editor", disabled=table_col) # Display table. Used over st.dataframe because this handles adjusting to the column width, 
                                                                                                                                     # and also allows checkboxes in tables
                                                                                                                                     # Disable all columns
                # Detect checked rows
                checked_index = edited_df.index[edited_df["View Details"]].tolist() # edited_df.index[...] keeps only indices where "View Details" is True i.e. checkbox is ticked

                # If any checkbox is checked, update session state and rerun
                if checked_index:
                    st.session_state["selected_filtered"] = checked_index[0]
                    st.rerun()


            ########################################
            ##### Table 3: Validated Incidents #####
            st.header("✅ Validated Incidents")

            ##### Table #####
            # Initialise column headers and empty row
            table_col = ["ID", "Longitude", "Latitude", "Road Name", "Date & Time", "Incident Type", "Incident Subtype", "Details", "Priority", "Status"]
            empty = ["...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]

            # If no validated incidents, display empty table
            if not st.session_state["validated"]:
                df = pd.DataFrame([empty],columns=table_col)
                df.index = ["🚨 No Records Found"] # Initialise serial number value as default value

            else:
                df = pd.DataFrame(st.session_state["validated"])
                df.columns = table_col # Rename columns  
                df.index = range(1, len(df) + 1) # Initialise serial number column to be one-indexed

            df.index.name = "S/N" # Rename index column
            df = df.drop(columns=["Details"]) # Remove "Details" column 

            df["View Details"] = [False] * len(df) # Add view details column

            styled_df = df.style.applymap(highlight_priority, subset=["Priority"])

            edited_df = st.data_editor(styled_df, use_container_width=True, key="validated_incidents_editor", disabled=table_col) # Display table. Used over st.dataframe because this handles adjusting to the column width, 
                                                                                                                                  # and also allows checkboxes in tables
            # Detect checked rows
            checked_index = edited_df.index[edited_df["View Details"]].tolist() # edited_df.index[...] keeps only indices where "View Details" is True i.e. checkbox is ticked

            # If any checkbox is checked, update session state and rerun
            if checked_index:
                st.session_state["selected_validated"] = checked_index[0]
                st.rerun()
        
            # Trademark 
            st.markdown("<p style='text-align: center;'>© 2025 OptiMove AI™.</p>", unsafe_allow_html=True)

        with archived:
            ####################################################
            ##### Table 1: Incoming Incidents (unfiltered) #####
            # TODO: table styles e.g. bolded headers or wtv
            st.header("📨 Incoming Incidents")

            # Initialise column headers and empty row
            table_col = ["ID", "Longitude", "Latitude", "Road Name", "Date & Time", "Incident Type", "Incident Subtype", "Details"]
            empty = ["...", "...", "...", "...", "...", "...", "...", "..."]

            # If no incoming incidents, display empty table
            if not st.session_state["incoming"]:
                df = pd.DataFrame([empty],columns=table_col)
                df.index = ["🚨 No Records Found"] # Initialise serial number value as default value

            else:
                df = pd.DataFrame(st.session_state["incoming"])
                df.columns = table_col # Rename columns  
                df.index = range(1, len(df) + 1) # Initialise serial number column to be one-indexed

            df.index.name = "S/N" # Rename index column
            df = df.drop(columns=["Details"]) # Remove "Details" column  
            st.data_editor(df, use_container_width=True, key="incoming_incidents_editor", disabled=df.columns.tolist()) # Display table. Used over st.dataframe because this handles adjusting to the column width. 
                                                                                        # Key to prevent streamlit.errors.StreamlitDuplicateElementId

            # Filter button
            #if st.button("Filter Incidents"):
                #st.session_state["incoming_to_filter"] = st.session_state["incoming"] # Store incidents to filter, which will be sent to backend
                #st.session_state["incoming"] = [] # Clear incoming data
                #st.rerun()





    # TODO
    # Is priority assignment necessary for jam incidents?

if __name__ == "__main__":
    main()