"""
Name:       Jason Porter
CS230:      Section 05
Data:       AirBnB
URL:        https://share.streamlit.io/porterjason/final-project/main/home.py

Description: This program acts as the home page to my other two applications,
            which are top_listings.py and listings_map.py

"""

import streamlit as st

# Links to programs
program1 = '[Find the Top Listings for You](https://share.streamlit.io/porterjason/final-project/main/top_listings.py)'
program2 = '[View Our Cambridge Listings](https://share.streamlit.io/porterjason/final-project/main/listings_map.py)'

# App Outputs

st.title("Welcome to AirBnB Cambridge")
st.subheader("How can we help you today?")
st.write("\n")
# Links to programs
st.markdown(program1, unsafe_allow_html=True)
st.markdown(program2, unsafe_allow_html=True)
