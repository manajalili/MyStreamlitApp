import streamlit as st
import requests
import numpy as np

st.markdown("# Streamlit Giphy")

if st.button("See Lewagon"):
    st.image("raw_data/wagon.png")
    
query = st.text_input("Search a giph")

if query:
    url = "https://api.giphy.com/v1/gifs/search"

    p = {"api_key": st.secrets.api_key, "q": query, "limit": 5 }

    response = requests.get(url=url, params=p).json()["data"]

    giph_url = response[np.random.randint(1,5)]["embed_url"]
    
    st.write(
        f'<iframe src="{giph_url}" width="480" height="300">',
        unsafe_allow_html=True
    )