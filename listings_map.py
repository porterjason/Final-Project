"""
Name:       Jason Porter
CS230:      Section 05
Data:       AirBnB
URL:        https://share.streamlit.io/porterjason/final-project/main/listings_map.py

Description: This program outputs a map of all listings that meet a set of
            parameters that are in a sidebar on the application webpage

            *** This is the application code hosted on streamlit. There is a seperate file
            listings_map_graph.py that includes matplotlib and further description ***

"""

import streamlit as st
import numpy as np
import pandas as pd

listings_f = pd.read_csv("listings.csv")

columns_list = ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'latitude', 'longitude', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'last_review', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
neighborhood_list = ['All Neighborhoods', 'Agassiz', 'Area 2/MIT', 'Cambridge Highlands', 'Cambridgeport', 'East Cambridge', 'Mid-Cambridge', 'Neighborhood Nine', 'North Cambridge', 'Riverside', 'Strawberry Hill', 'The Port', 'Wellington-Harrington', 'West Cambridge']
nights_slider_max = '5+'
nights_min = [1,2,3,4,'5+']
listing_types = ['All Types', 'Entire home/apt', 'Private room', 'Shared room']

df = pd.DataFrame(data=listings_f, columns=columns_list)
df.set_index('id', inplace=True)

def p2_filters(data):
    df_result = data

    # neighborhood filter
    if neighborhood == neighborhood_list[0]:
        df_result = df_result
    else:
        df_result = df_result[df_result['neighbourhood'] == neighborhood]

    # listing type filter
    if selected_type == listing_types[0]:
        df_result = df_result
    else:
        df_result = df_result[df_result['room_type'] == selected_type]

    # ProHost filter
    if prohost_check:
        df_result = df_result[df_result['calculated_host_listings_count'] >= 2]
        df_result = df_result[df_result['number_of_reviews'] > 25]

    # Max Price Filter
    df_result = df_result[df_result['price'] <= max_price]

    return df_result  # returns listings query

# SIDEBAR OUTPUT

st.sidebar.header("Thank you for using AirBnB")

# Select Neighborhood
neighborhood = st.sidebar.radio("Choose a Neighborhood: ", neighborhood_list)

# Select Listing Type
selected_type = st.sidebar.radio("Select Listing Types: ", listing_types)

# Prohost Check
prohost_check = st.sidebar.checkbox("View Only ProHost Owned Listings: ", False)

# Max Price Slider
min_slider = int(df['price'].min())
max_slider = int(df['price'].max())
max_price = st.sidebar.slider('Maximum Price ($): ', min_slider, max_slider)

# Links back to Main Page and Other Program

menu = '[Return to Home](https://share.streamlit.io/porterjason/final-project/main/home.py)'
program1 = '[Find the Top Listings for You](https://share.streamlit.io/porterjason/final-project/main/top_listings.py)'

st.sidebar.markdown(menu, unsafe_allow_html=True)
st.sidebar.markdown(program1, unsafe_allow_html=True)

# MAIN OUTPUT

data = p2_filters(df)

st.title("Our Cambridge, MA Listings")

# Map data after filters
coordinates = {'latitude': [], 'longitude': []}
for index, row in data.iterrows():
    coordinates['latitude'].append(row['latitude'])
    coordinates['longitude'].append(row['longitude'])

map_data = pd.DataFrame(data=coordinates , columns=['latitude', 'longitude'])
st.map(map_data)

# Continue to listings_map_graph.py
