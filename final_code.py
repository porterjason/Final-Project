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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import statistics
from datetime import datetime, timedelta

listings_f = pd.read_csv("listings.csv")
columns_list = ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'latitude', 'longitude', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'last_review', 'reviews_per_month', 'calculated_host', 'listings_count', 'availability_365']
nights_slider_max = '5+'
listing_types = ['Entire home/apt', 'Private room', 'Shared room']

df = pd.DataFrame(data=listings_f, columns=columns_list)
df.set_index('id', inplace=True)

price = 100
result = df[df['minimum_nights'] >= 3]
# print(result['minimum_nights'].min())


def p1_filters(data):
    df_result = data

    # nights filter
    if nights == nights_slider_max:
        df_result = df_result
    else:
        df_result = df_result[df_result['minimum_nights'] <= nights]
    # listing type filter
    df_result = df_result[df_result['room_type'] == selected_type]

    return df_result  # returns listings query


# Select Nights
# nights = st.sidebar.radio("How many nights will you be staying?", nights_min)
nights = '5+'

# Select Listing Type
# selected_type = st.selectbox("Select Listing Types:", listing_types)
selected_type = 'Entire home/apt'

# Prohost check
prohost_check = st.checkbox("Do you only want to see certified P")

# Test
data = p1_filters(df)
print(data['minimum_nights'].min())
print(data['minimum_nights'].max())
