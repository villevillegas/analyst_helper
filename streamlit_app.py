import streamlit as st
import pandas as pd
from io import StringIO

st.write("Hello Worldssss")

uploaded_file = st.file_uploader("Choose a file")


def check_data(dataframe, head=5):
    st.write(" SHAPE ".center(70,'-'))
    st.write('Rows: {}'.format(dataframe.shape[0]))
    st.write('Columns: {}'.format(dataframe.shape[1]))
    st.write(" TYPES ".center(70,'-'))
    st.write(dataframe.dtypes)
    st.write(" HEAD ".center(70,'-'))
    st.write(dataframe.head(head))
    st.write(" TAIL ".center(70,'-'))
    st.write(dataframe.tail(head))
    st.write(" MISSING VALUES ".center(70,'-'))
    st.write(dataframe.isnull().sum())
    st.write(" DUPLICATED VALUES ".center(70,'-'))
    st.write(dataframe.duplicated().sum())
    #st.write(" QUANTILES ".center(70,'-'))
    #st.write(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

if uploaded_file is not None:
    st.write(""" ### Exploration begins...""")
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    check_data(dataframe)
