# Real-Time-Crypto-Trend-AI

# Overview
This repository features an AI-powered cryptocurrency trend analysis application that delivers real-time market direction insights. Leveraging advanced LLMs from Groq and live CoinGecko API data, the system identifies whether a cryptocurrency is in an uptrend or downtrend. It is built using Streamlit for a seamless, interactive user experience.

# Abstract
This project integrates a large language model with live crypto pricing APIs to analyze and classify the market trend (uptrend or downtrend) for any user-specified cryptocurrency. Using Groq’s LLaMA 3.3 70B model and a clean custom UI, the system offers fast, concise, and visually appealing insights for traders and enthusiasts.

# Introduction
The purpose of this project is to develop an intelligent system that can:

  - Fetch live prices of cryptocurrencies via the CoinGecko API.

  - Use a Groq-hosted LLM agent to interpret price data and identify market trends.

  - Display results with an intuitive and modern frontend using Streamlit and custom CSS.

  - Allow users to input any crypto symbol for on-demand analysis.

# Problem Statement
Crypto traders and investors often seek quick, reliable insights into market trends. However, many tools are either overloaded with data or require manual technical analysis. This project simplifies trend detection using a natural language interface, real-time pricing, and AI-backed logic.

# Motivation
- **Instant Market Feedback:** Provides users with immediate trend classification.

- **AI-Powered Simplicity:** Uses a language model to abstract away technical complexities.

- **Real-Time Price Feed:** Fetches the latest prices directly from CoinGecko.

- **Clean UI:** Features a minimal, accessible interface with responsive design.

- **Scalability:** Framework supports adding new features such as trend history, visualizations, or other market indicators.

- **LLM Integration:** Demonstrates practical use of language models in financial applications.

# Key Points
- **LLM Agent Integration:** Utilizes Groq’s LLaMA-3.3 70B model for decision-making.

- **CoinGecko API:** Pulls real-time price data for any valid cryptocurrency.

- **Minimalist UX:** Designed using Streamlit with custom CSS for a polished, user-friendly layout.

- **Trend-Only Output:** Clearly labels the trend as either "Uptrend 📈" or "Downtrend 📉" to avoid information overload.

- **Error Handling:** Gracefully manages user input errors and unavailable crypto tickers.

- **Reusable Architecture:** Modular agent design allows easy extension to additional financial metrics.
