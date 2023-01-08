import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 Streamlit Example App')

st.write('Hello world!')

# Input widgets inside column container
col1, col2 = st.columns(2, gap="medium")
with col1:
    genre = st.radio(
        "What\'s your favorite movie genre",
        ('Comedy', 'Drama', 'Documentary', 'Romance', 'Action', 'Suspense'))

    st.write(f"You choose {genre}")

with col2:
    if st.button('Click for magic! ✨'):
        st.snow()
