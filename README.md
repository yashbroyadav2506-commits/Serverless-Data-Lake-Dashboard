# ☁️ Serverless Sales Data Lake & Dashboard

An end-to-end data pipeline that ingests raw sales data, catalogs it in a serverless data lake, queries it using SQL, and visualizes the insights on an interactive dashboard.

## 🏗️ Architecture
1. **Storage**: Amazon S3 (Data Lake)
2. **Cataloging**: AWS Glue Crawler
3. **Query Engine**: Amazon Athena
4. **Visualization**: Python, Pandas, Streamlit, Plotly

## 💡 Key Insights Discovered
*   Electronics generate the highest overall revenue, but Office Supplies have a comparable profit margin.
*   New York, Florida, and California account for over 50% of total sales.
*   *(Add any trend you see in the monthly line chart here)*

## 🚀 How to Run Locally
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `streamlit run app.py`
