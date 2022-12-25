import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 Streamlit Example App')

st.write('Hello world!')

st.subheader('Beautiful Charts 🤩')
# Charts inside container element
tab1, tab2 = st.tabs(["Bar Chart 📊", "Area chart 📈"])
with tab1:
   chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=["a", "b", "c"])

   st.bar_chart(chart_data)

with tab2:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.area_chart(chart_data)

# Button element
if st.button('Click for magic! ✨'):
    st.snow()
