import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('TEST APPS')


st.title('APPS')

df=pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[35.69,139.76],
    columns=['lat','lon']
)

print(df)

st.map(df)