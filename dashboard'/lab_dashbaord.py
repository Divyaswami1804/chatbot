import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="lab Monitoring dashboard", layout="wide")
st.title("Real time lab monitoring Dashboard")

df = pd.read_csv("data/lab_data.csv")

