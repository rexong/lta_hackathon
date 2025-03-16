import streamlit as st
import pandas as pd

##### ✅ Step 1: Initialize Test Data #####
if "validated" not in st.session_state:
    st.session_state["validated"] = [
        {"ID": 101, "Longitude": 103.851, "Latitude": 1.290, "Road Name": "Orchard Rd", 
         "Date & Time": "2025-03-07 12:00", "Incident Type": "Hazard", 
         "Incident Subtype": "Car Stopped", "Priority": "High"},
        
        {"ID": 102, "Longitude": 103.852, "Latitude": 1.291, "Road Name": "Marina Bay",
         "Date & Time": "2025-03-07 12:30", "Incident Type": "Jam", 
         "Incident Subtype": "Heavy Traffic", "Priority": "Medium"},
        
        {"ID": 103, "Longitude": 103.853, "Latitude": 1.292, "Road Name": "Changi Airport",
         "Date & Time": "2025-03-07 13:00", "Incident Type": "Road Closed", 
         "Incident Subtype": "Event Closure", "Priority": "Low"}
    ]

df = pd.DataFrame(st.session_state["validated"])
df.index = range(1, len(df) + 1)  # Set row index to start from 1
df.index.name = "S/N"

##### ✅ Step 2: Initialize Dispatch Status in Session State #####
if "dispatch_status" not in st.session_state:
    st.session_state["dispatch_status"] = {row["ID"]: False for row in st.session_state["validated"]}

# ✅ Step 3: Create Dispatch Column Based on Session State
df["Dispatch"] = df["ID"].apply(lambda x: st.session_state["dispatch_status"].get(x, False))

##### 🚀 Step 4: Render Editable Table with Checkboxes #####
edited_df = st.data_editor(df, use_container_width=True, key="dispatch_table", column_config={
    "Dispatch": st.column_config.CheckboxColumn("Dispatch")  # No `disabled`, we handle it manually
})

##### ✅ Step 5: Detect Checked Checkboxes and Lock Them #####
for i, row in edited_df.iterrows():
    if row["Dispatch"] and not st.session_state["dispatch_status"][row["ID"]]:  
        st.session_state["dispatch_status"][row["ID"]] = True  # Lock the checkbox permanently
        st.rerun()  # Refresh UI to lock the checkbox