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

st.write("Hello world")


menu = '[Return to Home](https://share.streamlit.io/porterjason/final-project/main/home.py)'
program1 = '[View Our Cambridge Listings](https://share.streamlit.io/porterjason/final-project/main/top_listings.py)'

st.sidebar.markdown(menu, unsafe_allow_html=True)
st.sidebar.markdown(program1, unsafe_allow_html=True)
