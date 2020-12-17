"""
Name:       Your Name
CS230:      Section 05
Data:       AirBnB
URL:        Link to your web application online (see extra credit)

Description: This project creates

This program ... (a few sentences about your program and the queries and charts)

"""
# interactive data-driven web-based Python application that shows your mastery of
# many coding concepts as you interact with data real world data

import streamlit as st

# Links to programs
program1 = '[Find the Top Listings for You](https://share.streamlit.io/porterjason/final-project/main/top_listings.py)'
program2 = '[View Our Cambridge Listings](https://share.streamlit.io/porterjason/final-project/main/listings_map.py)'

# App Outputs

st.title("Welcome to AirBnB Cambridge")
st.subheader("How can we help you today?")

# Links to programs
st.sidebar.markdown(program1, unsafe_allow_html=True)
st.sidebar.markdown(program2, unsafe_allow_html=True)
