import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

'As Dataframe'
st.dataframe(dataframe.style.highlight_max(axis=0))

'As table'
st.table(dataframe)

'As JSON'
st.json({
    'dataframe': dataframe.to_dict(),
    'columns': list(dataframe.columns),
})

'As Dataframe'
dataframe
