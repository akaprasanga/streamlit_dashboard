# streamlit_app.py
import os
import streamlit as st
from st_files_connection import FilesConnection
st.header("Welcome to the dashboard!")


# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

content = read_file("streamlit-maket-data/test-data/dummy_data.csv")

st.write(content)

# Print results.
# for row in df.itertuples():
#     st.write(f"{row.Owner} has a :{row.Pet}:")
