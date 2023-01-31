import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 Streamlit Example App')

st.write('Hello world!')

st.subheader('Beautiful Charts 👀')

# Charts inside container element
tab1, tab2 = st.tabs(["Bar Chart 📊", "Area chart 📈"])
with tab1:
   chart_1 = pd.DataFrame(
       np.random.randn(20, 3),
       columns=["a", "b", "c"])

   st.bar_chart(chart_1)

with tab2:
    chart_2 = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.area_chart(chart_2)
    
genre = st.radio(
    "What\'s your favorite movie genre 🎬",
    ('Comedy', 'Drama', 'Documentary', 'Action', 'Romance'))

st.write(f"You selected: {genre}")

# Button element
if st.button('Click for magic! ✨'):
    st.snow()
