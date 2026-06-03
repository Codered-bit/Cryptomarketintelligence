

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

Crypto Market Intelligence Dashboard

Overview

The Crypto Market Intelligence Dashboard is a real-time cryptocurrency monitoring and anomaly detection system built using Python and Streamlit.

The application retrieves live market data from the CoinGecko API and transforms raw market information into actionable insights through comparative analysis, liquidity scoring, performance ranking, and statistical anomaly detection.

This project demonstrates practical skills in:

* Data collection and API integration
* Data cleaning and transformation
* Financial market analysis
* Statistical anomaly detection
* Dashboard development
* Data visualization

⸻

Business Problem

Cryptocurrency markets generate large volumes of data that can be difficult to monitor efficiently.

Traders, analysts, and liquidity providers need tools that can:

* Monitor multiple assets simultaneously
* Identify unusual market behaviour
* Compare market activity across assets
* Generate actionable market intelligence

This project provides a framework for monitoring market conditions and highlighting significant changes in market activity.

⸻

Features

Real-Time Market Monitoring

Tracks major cryptocurrency assets including:

* Bitcoin (BTC)
* Ethereum (ETH)
* BNB
* Solana (SOL)
* XRP

Market Overview

Displays:

* Current Price
* Market Capitalization
* Trading Volume
* 24-Hour Performance

Performance Ranking

Ranks assets by 24-hour performance to identify:

* Top-performing assets
* Underperforming assets
* Relative market strength

Liquidity Score

Generates a simple liquidity score based on:

* Market Capitalization
* Trading Volume

This provides a quick indication of the relative liquidity profile of each asset.

Anomaly Detection

Applies Z-score analysis to identify unusual market behaviour.

Assets exhibiting statistically significant deviations are flagged as potential anomalies for further investigation.

Market Health Score

Provides a simplified indicator of overall market stability based on observed market conditions.

⸻

Methodology

Data Source

Market data is retrieved from the CoinGecko API.

Metrics collected include:

* Current Price
* Market Capitalization
* Trading Volume
* 24-Hour Price Change

Statistical Analysis

The project uses Z-score normalization:

Z = (X − μ) / σ

Where:

* X = Current observation
* μ = Mean value
* σ = Standard deviation

Assets with absolute Z-scores above the defined threshold are flagged as anomalous.

Liquidity Score

A composite liquidity score is calculated using normalized:

* Trading Volume
* Market Capitalization

This score provides a simplified proxy for market liquidity.

⸻

Technology Stack

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Requests
* CoinGecko API

⸻

Project Structure

.
├── app.py
├── requirements.txt
├── README.md
└── screenshots/

⸻

Example Dashboard Components

* Market Overview Table
* Performance Ranking
* Trading Volume Comparison
* Market Capitalization Comparison
* Liquidity Score Analysis
* Market Health Score
* Anomaly Detection Alerts

⸻

Potential Applications

This framework can be extended for:

* Crypto market surveillance
* Liquidity monitoring
* Trading operations
* Market maker evaluation
* DeFi analytics
* Risk monitoring

⸻

Future Improvements

Planned enhancements include:

* Multi-day historical data collection
* Advanced anomaly detection models
* Machine learning-based market classification
* Market maker performance analytics
* Incentive mechanism simulation
* Multi-exchange data integration

⸻

About the Author

Dare Shonubi

* MSc Financial Technology & Trading
* BSc Data Science
* BSc Business Administration
* Google Data Analytics Professional Certificate
* Blockchain and Cryptocurrency Certifications

This project was developed as part of a broader portfolio focused on cryptocurrency markets, data analytics, and liquidity intelligence.
