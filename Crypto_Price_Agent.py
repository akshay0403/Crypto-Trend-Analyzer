import streamlit as st
import requests
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(
    page_title="Crypto Trend Analyzer",
    page_icon="📈",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    :root {
        --primary-color: #4A6FFF;
        --secondary-color: #344054;
        --background-color: #F9FAFB;
        --text-color: #1D2939;
        --light-gray: #EAECF0;
    }

    .stApp { background-color: var(--background-color); }
    .main-title {
        color: var(--text-color);
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 32px;
        margin-bottom: 8px;
        padding-top: 20px;
    }
    .subtitle {
        color: var(--secondary-color);
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 16px;
        margin-bottom: 25px;
        opacity: 0.8;
    }
    .stButton>button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: 500;
        font-size: 16px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #3A5CD0;
    }
    .stTextInput>div>div>input {
        border-radius: 6px;
        border: 1px solid var(--light-gray);
        padding: 12px 16px;
        font-size: 16px;
    }
    .stTextInput>div>div>input:focus {
        border-color: var(--primary-color);
    }
    .info-box {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(16, 24, 40, 0.1);
        text-align: center;
        font-size: 18px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='main-title'>Crypto Trend Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Powered by Groq + CoinGecko API</div>", unsafe_allow_html=True)

# Agent setup
agent = Agent(
    name="Crypto Analyst",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "You are a crypto trend expert.",
        "Given the current price of a coin, respond with only: 'Uptrend 📈' or 'Downtrend 📉'.",
        "No explanation or financial advice — only a clear trend indication."
    ],
    markdown=True
)

# Input
coin = st.text_input("", placeholder = "Enter The Crypto Here ...").strip().lower()


# Submit button
if st.button("Check Trend"):
    if coin:
        with st.spinner("Analyzing trend..."):
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
            try:
                data = requests.get(url).json()
                price = data.get(coin, {}).get("usd", "N/A")

                if price == "N/A":
                    st.error("Coin not found. Please check your input.")
                else:
                    response = agent.run(
                        f"The current price of {coin} is ${price}. Is it in an uptrend or downtrend?"
                    ).content.replace("#", "").strip()

                    # Side-by-side layout
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("<div class='info-box'><b>Current Price</b><br>${:.2f}<br></div>".format(price), unsafe_allow_html=True)
                    with col2:
                        st.markdown(f"<div class='info-box'><b> Trend </b><br>{response}<br></div>", unsafe_allow_html=True)
            except Exception as e:
                st.error("Something went wrong.")
                st.exception(e)
    else:
        st.warning("Please enter a cryptocurrency name.")
