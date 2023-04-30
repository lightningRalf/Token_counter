import streamlit as st
from transformers import AutoTokenizer
import requests
import datetime
from dateutil.relativedelta import relativedelta

# Count tokens in a text string using a specified language model.
def count_tokens_text(text, model_name='gpt4'):
    # (same as before)

# Fetch the most popular models from the last month
def get_popular_models():
    one_month_ago = (datetime.datetime.now() - relativedelta(months=1)).strftime("%Y-%m-%d")
    api_url = f"https://huggingface.co/api/models?sort=downloads&direction=desc&start_date={one_month_ago}"
    response = requests.get(api_url)
    data = response.json()
    popular_models = [model["modelId"] for model in data["results"]]
    return popular_models

# Streamlit app
st.title("Token Counter")
text = st.text_area("Text:", value="", height=200)

popular_models = get_popular_models()
model_name = st.selectbox("Model:", options=popular_models, index=0)
manual_entry = st.text_input("Or enter a model manually:", value="")
if manual_entry:
    model_name = manual_entry

if st.button("Count Tokens"):
    token_count, error = count_tokens_text(text, model_name)
    if token_count is not None:
        st.success(f"Token count: {token_count}")
    elif error is not None:
        st.error(f"Error: {error}")
