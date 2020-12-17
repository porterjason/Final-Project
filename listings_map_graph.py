"""
Name:       Jason Porter
CS230:      Section 05
Data:       AirBnB
Filename:   listings_map_graph

Description: This program is an extension of listings_map.py that includes a graph
            of average prices by a parameter. For some reason Matplotlib does not work on
            Streamlit share, so I have included this bonus file with the graph I
            was hoping to include online.

"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

listings_f = pd.read_csv("listings.csv")

columns_list = ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'latitude', 'longitude', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'last_review', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
neighborhood_list = ['All Neighborhoods', 'Agassiz', 'Area 2/MIT', 'Cambridge Highlands', 'Cambridgeport', 'East Cambridge', 'Mid-Cambridge', 'Neighborhood Nine', 'North Cambridge', 'Riverside', 'Strawberry Hill', 'The Port', 'Wellington-Harrington', 'West Cambridge']
listing_types = ['All Types', 'Entire home/apt', 'Private room', 'Shared room']

df = pd.DataFrame(data=listings_f, columns=columns_list)
df.set_index('id', inplace=True)


# Filter data for graph
def graph(data, x_axis):
    graph_data = {}
    if x_axis == 'Neighborhood':
        for hood in neighborhood_list:
            temp_data = df
            if hood == 'All Neighborhoods':
                temp_list = temp_data['price'].tolist()
                avg = np.average(temp_list)
                graph_data[hood] = avg
            else:
                temp_data = temp_data[temp_data['neighbourhood'] == hood]
                temp_list = temp_data['price'].tolist()
                avg = np.average(temp_list)
                graph_data[hood] = avg
    elif x_axis == 'Listing Type':
        for types in listing_types:
            temp_data = df
            if types == 'All Types':
                temp_list = temp_data['price'].tolist()
                avg = np.average(temp_list)
                graph_data[types] = avg
            else:
                temp_data = temp_data[temp_data['room_type'] == types]
                temp_list = temp_data['price'].tolist()
                avg = np.average(temp_list)
                graph_data[types] = avg

    return graph_data


# Creates Chart
def bar_chart(data, labels):
    for b in labels:
        plt.bar(b, data[b], label=b)

    plt.show()


# Outputs that would be below Mapbox

st.header("Visualized Pricing for Our Listings")
x_axis = st.radio("Graph Average Price By: ", ['Neighborhood', 'Listing Type'])

group = []
if x_axis == 'Neighborhood':
    group = neighborhood_list
else:
    group = listing_types

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(bar_chart(graph(df, x_axis), group))
