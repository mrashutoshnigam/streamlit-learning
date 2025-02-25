import streamlit as st
import pandas as pd

st.text("Hello, World!")

df= pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 24, 3, 27]
})
st.table(df)
st.write(df)

st.line_chart(df)