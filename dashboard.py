import streamlit as st
import pandas as pd

st.title("Simple Dashboard")
df = pd.DataFrame(
    {"Month": ["Jan", "Feb", "Mar", "Apr"],
     "Sales": [100, 150, 120, 200],
     }
)
st.line_chart(df.set_index("Month"))
st.dataframe(df)
