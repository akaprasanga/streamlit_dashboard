import streamlit as st
import pandas as pd
import plotly.express as px
from secrects_manager import secrets
import boto3
from boto3.dynamodb.conditions import Key, Attr
import datetime

st.title("Crypto currency Price with Social Media Sentiment")

dynamodb = boto3.resource('dynamodb', aws_access_key_id=secrets.AWS_ACCESS_KEY_ID, aws_secret_access_key=secrets.AWS_ACCESS_KEY_SECRETS,region_name='us-east-1')
table = dynamodb.Table('marketcapdata')
response = table.query(
    KeyConditionExpression=Key('currency').eq('BTC'),
    FilterExpression=Attr('data.last_updated').between('2023-07-11T00:00:00Z','2023-07-14T00:00:00Z'))

if response['Count'] > 0 and response['ResponseMetadata']['HTTPStatusCode'] == 200:
    df = pd.DataFrame(response['Items'])
    df['data'] = df['data'].apply(lambda x: x['price'])
    print(df)
else:
    print("No data found")

st.title("Bitcoin Price")
fig = px.line(df, x='last_updated', y='data', title='Bitcoin Price').update_layout(xaxis_title='Date UTC-0', yaxis_title='Price in USD')
st.plotly_chart(fig)
