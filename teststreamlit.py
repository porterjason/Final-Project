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
link = '[GitHub](http://github.com)'
submit = st.button('submit new letters')
if submit:
    "Hey there"
    st.markdown(link, unsafe_allow_html=True)

from bokeh.models.widgets import Div

if st.button('Go to Streamlit'):
    js = "window.open('https://www.streamlit.io/')"  # New tab or window
    js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
