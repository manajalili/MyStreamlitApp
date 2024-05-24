import requests
import streamlit as st
import numpy as np

st.markdown("# Streamlit Giphy")

if st.button("See Le wagon"):
    st.image("raw_data/wagon.png")
    
query = st.text_input("Look up a GIF!")
url = "https://api.giphy.com/v1/gifs/search"
params = {"api_key": st.secrets["api_key"], "q": query, "limit": 5}
response = requests.get(url=url, params=params).json()['data']

while not query:
    st.stop()
    
gif_url = response[np.random.randint(1,5)]["embed_url"]
# st.write(gif_url)

st.write(
    f'<iframe src="{gif_url}" width="480" height="240">',
    unsafe_allow_html=True,
)