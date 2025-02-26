import streamlit as st
import pandas as pd
import numpy as np

st.text("Hello, World!")
st.text("This is a Streamlit app created by Ashutosh Nigam")

st.link_button("Click here to visit my LinkedIn profile", "https://www.linkedin.com/in/mrashutoshnigam")
st.balloons()
st.success("This is a success message")
# Create a simple dataframe
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.dataframe(df)
# Create a line chart
st.line_chart(df)