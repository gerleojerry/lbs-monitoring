import os
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from supabase import create_client, Client

from utils import format_number, col_design

load_dotenv()
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_ANON_KEY')

st.set_page_config(
    page_title="LBS Usage Tracking",
    # page_icon="🏂",
    page_icon="LBS",
    layout="wide",
    initial_sidebar_state="expanded")

# alt.themes.enable("dark")


supabase: Client = create_client(supabase_url, supabase_key)
data = supabase.table('usage').select('*').execute()

df = pd.DataFrame(data.data)

total : int = df['cost'].sum()
token : int = df['token'].sum()



st.header("Dashboard for the LBS Usage")

top_col = st.columns((2, 2), gap='medium')


service_tokens = df.groupby(by = 'service').agg({'cost' : 'sum'})


with top_col[0]:
    html = col_design("Total Cost", f"${total}" )
    
    st.markdown(html, unsafe_allow_html=True)

with top_col[1]:
     
    html = col_design("Total Token", f"{token}" )
    
    st.markdown(html, unsafe_allow_html=True)


st.subheader("Usage Per Service")

service_cols = st.columns((2, 2), gap='medium')
service_tokens = df.groupby(by = 'service').agg({'cost' : 'sum'})
token_counts = df.groupby(by = 'service').agg({'token' : 'sum'})


with service_cols[0]:
    
    fig, ax = plt.subplots()
    service_tokens.plot(kind='bar', ax=ax)
    ax.set_xlabel('Service', fontsize = '10')
    ax.set_ylabel('Amount')
    ax.set_title('Amount Used per Service')
    st.pyplot(fig)


with service_cols[1]:

    fig, ax = plt.subplots()
    token_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('Service')
    ax.set_ylabel('Tokens Used')
    ax.set_title('Tokens Used per Service')
    st.pyplot(fig)


st.subheader("Usage Per Customer")

customers = df.groupby(by = 'user' ).agg( { "token" : "sum", 'cost' : 'sum' } ).reset_index()
     
st.dataframe(customers)