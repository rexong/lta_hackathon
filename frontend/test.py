import streamlit as st
from streamlit_javascript import st_javascript

st.title("Interactive JavaScript Example")

# ✅ JavaScript to detect button clicks
js_code = """
document.getElementById("myButton").addEventListener("click", function() {
    window.streamlit_javascript.returnValue("clicked");
});
"""

# ✅ Create a button using HTML
st.markdown(
    """
    <button id="myButton" style="
        padding: 10px 20px;
        font-size: 18px;
        background-color: #0072ff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    ">Click Me!</button>
    """,
    unsafe_allow_html=True,
)

# ✅ Capture JavaScript output
button_clicked = st_javascript(js_code=js_code)

# ✅ Update session state when button is clicked
if button_clicked == "clicked":
    st.session_state["button_clicked"] = True
    st.rerun()

# ✅ Display message when button is clicked
if "button_clicked" in st.session_state:
    st.success("🎉 JavaScript detected the button click!")