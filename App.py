app.py
import streamlit as st
import requests
import pandas as pd
import numpy as np

# -----------------------------
# CONFIG
# -----------------------------

COINS = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "BNB": "binancecoin",
    "Solana": "solana",
    "XRP": "ripple"
}

WINDOW_SIZE = 20
Z_THRESHOLD = 1.5

st.set_page_config(page_title="Crypto Market Intelligence", layout="wide")

st.title("📊 Crypto Market Intelligence Dashboard")

st.markdown("""
Real-time crypto market monitoring with anomaly detection using CoinGecko data.
""")

# -----------------------------
# API FUNCTION
# -----------------------------

def get_market_overview():

    url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        "?vs_currency=usd"
        "&ids=bitcoin,ethereum,binancecoin,solana,ripple"
    )

    response = requests.get(url)

    if response.status_code != 200:
        st.error("API Error")
        return []

    return response.json()

# -----------------------------
# LOAD DATA
# -----------------------------

data = get_market_overview()

df = pd.DataFrame([
    {
        "Asset": coin["symbol"].upper(),
        "Price": coin["current_price"],
        "Market Cap": coin["market_cap"],
        "Volume": coin["total_volume"],
        "24h Change": coin["price_change_percentage_24h"]
    }
    for coin in data
])

# -----------------------------
# MARKET OVERVIEW
# -----------------------------

st.subheader("🌍 Market Overview")

st.dataframe(df, use_container_width=True)

# -----------------------------
# TOP PERFORMER
# -----------------------------

top = df.sort_values("24h Change", ascending=False).iloc[0]

st.success(
    f"🏆 Top Performer: {top['Asset']} ({top['24h Change']:.2f}%)"
)

# -----------------------------
# Z-SCORE ANALYSIS
# -----------------------------

metrics = ["Price", "Market Cap", "Volume", "24h Change"]

for m in metrics:
    df[f"{m}_Z"] = (
        (df[m] - df[m].mean()) / df[m].std()
    )

df["Anomaly"] = df["24h Change_Z"].abs() > Z_THRESHOLD

# -----------------------------
# ANOMALIES
# -----------------------------

st.subheader("⚠️ Anomaly Detection")

anomalies = df[df["Anomaly"]]

if len(anomalies) > 0:
    st.warning("Anomalies detected in market behavior")
    st.dataframe(anomalies)
else:
    st.success("No major anomalies detected")

# -----------------------------
# CHARTS
# -----------------------------

st.subheader("📈 Volume Comparison")

st.bar_chart(df.set_index("Asset")["Volume"])

st.subheader("🏦 Market Cap Comparison")

st.bar_chart(df.set_index("Asset")["Market Cap"])

st.subheader("📊 24h Performance")

st.bar_chart(df.set_index("Asset")["24h Change"])
