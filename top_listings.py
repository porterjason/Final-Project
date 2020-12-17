"""
Name:       Jason Porter
CS230:      Section 05
Data:       AirBnB
URL:        https://share.streamlit.io/porterjason/final-project/main/top_listings.py

Description: This program takes in several parameters from the application user, 
                then puts out a top-ten recommendations list into a table

"""

import streamlit as st
import numpy as np
import pandas as pd

listings_f = pd.read_csv("listings.csv")
columns_list = ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'latitude', 'longitude', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'last_review', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
nights_slider_max = '5+'
nights_min = [1,2,3,4,'5+']
listing_types = ['Entire home/apt', 'Private room', 'Shared room']

df = pd.DataFrame(data=listings_f, columns=columns_list)
df.set_index('id', inplace=True)


def p1_filters(data):
    df_result = data

    # nights filter
    if nights == nights_slider_max:
        df_result = df_result
    else:
        df_result = df_result[df_result['minimum_nights'] <= nights]
    # listing type filter
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
# Select Nights
nights = st.sidebar.radio("How many nights will you be staying?", nights_min)
# Select Listing Type
selected_type = st.sidebar.selectbox("Select Listing Types:", listing_types)

# Prohost Check
prohost_check = st.sidebar.checkbox("View Only ProHost Owned Listings:", False)

# Max Price Slider
min_slider = int(df['price'].min())
max_slider = int(df['price'].max())
max_price = st.sidebar.slider('Maximum Price ($):', min_slider, max_slider)

# Links back to Main Page and Other Program

menu = '[Return to Home](https://share.streamlit.io/porterjason/final-project/main/home.py)'
program2 = '[View Our Cambridge Listings](https://share.streamlit.io/porterjason/final-project/main/listings_map.py)'

st.sidebar.markdown(menu, unsafe_allow_html=True)
st.sidebar.markdown(program2, unsafe_allow_html=True)

# Getting top 10
data = p1_filters(df)
temp_10 = data.sort_values(by=['reviews_per_month', 'price'])[0:10]
df_top10 = pd.DataFrame(data=temp_10, columns=columns_list)
df_top10['Rank'] = range(1, 1+len(df_top10))

# MAIN OUTPUT

st.title("Find the Top Cambridge, MA Listings!")
df_top10[['Rank', 'name', 'host_name','neighbourhood', 'price','last_review']]

# Select Listing
names = {}
for index, row in df_top10.head().iterrows():
     names[row['name']] = index
pick = st.selectbox("Select a Listing:", [*names])
id = str(names[pick])
link = "[AirBnB.com](https://www.airbnb.com/rooms/" + id + "?check_in=2021-01-03&check_out=2021-01-09&source_impression_id=p3_1608181766_Y1LPm0pldTru8zdS)"

# Get link to AirBnB
click = st.button('Get Link to Listing:')
if click:
    st.markdown(link, unsafe_allow_html=True)
