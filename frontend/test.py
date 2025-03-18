import streamlit as st

# Inject CSS to style tabs
st.markdown("""
    <style>
        div[role="tablist"] {
            background-color: #f0f2f6; /* Light grey background */
            border-radius: 10px;
            padding: 5px;
        }
        div[role="tab"] {
            font-size: 18px;
            color: black;
            padding: 10px;
            margin-right: 10px;
            border-radius: 10px;
            background: white;
        }
        div[role="tab"]:hover {
            background: #4CAF50; /* Green hover effect */
            color: white;
        }
        div[role="tab"][aria-selected="true"] {
            background: #4CAF50; /* Active tab color */
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Define tabs
tab1, tab2 = st.tabs(["Home", "Dashboard"])

with tab1:
    st.header("Home Page")
    st.write("This is the home screen.")

with tab2:
    st.header("Dashboard")
    st.write("This is the dashboard screen.")