import streamlit as st
import numpy as np
import pandas as pd

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

submit = st.button('submit new letters')
if submit:
    "Hey there"
link = '[GitHub](http://github.com)'
st.markdown(link, unsafe_allow_html=True)
