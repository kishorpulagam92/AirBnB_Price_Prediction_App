import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

def app():
    st.title('Pandas-Profiling Report')

    st.write('Progiling Report for Iris dataset.')
    iris = pd.read_csv("https://raw.githubusercontent.com/dxc-technology/DXC-Industrialized-AI-Starter/master/dxc/ai/datasets/data/iris.csv")
    pr = iris.profile_report()

    st_profile_report(pr)