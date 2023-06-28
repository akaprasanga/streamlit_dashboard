# streamlit_app.py
import os
import s3fs
import streamlit as st
from st_files_connection import FilesConnection
import boto3
import pandas as pd

st.header("Welcome to the Market dashboard!")

s3 = boto3.client('s3', aws_access_key_id=st.secrets['AWS_ACCESS_KEY_ID'], aws_secret_access_key=st.secrets['AWS_SECRET_ACCESS_KEY'])  
file_obj = s3.get_object(Bucket =st.secrets['BUCKET_NAME'], Key=st.secrets['FILE_PATH'])

if file_obj['ResponseMetadata']['HTTPStatusCode'] == 200:
    st.write('Success')
    file_content = file_obj['Body']
    df = pd.read_csv(file_content)
    st.write(df)
else:
    st.write('Error loading data from S3')
