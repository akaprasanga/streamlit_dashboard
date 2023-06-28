# streamlit_app.py
import os
import s3fs
import streamlit as st
from st_files_connection import FilesConnection
import boto3
import pandas as pd

st.header("Welcome to the dashboard!")

s3 = boto3.resource('s3', aws_access_key_id=st.secrets['AWS_ACCESS_KEY_ID'], aws_secret_access_key=st.secrets['AWS_SECRET_ACCESS_KEY'])  
bucket_name = s3.bucket(st.secrets['BUCKET_NAME'])
s3_filename = 'test-data/dummy_data.csv'
# obj = s3.Object(bucket_name, s3_filename)

for obj in bucket_name.objects.all():
    print(obj.key)

st.stop()
st.write(initial_df)
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
