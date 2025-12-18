# Keystone-Internship-Project

📊 Production Efficiency & Reporting System – Codebase

This repository contains the Python source code for a Production Efficiency and Reporting System that simulates industrial production data, applies machine learning for downtime prediction, generates analytical visualizations, and provides an interactive dashboard using Streamlit.

The project is inspired by real-world manufacturing analytics use cases in industrial automation environments such as Keystone Automation Solutions Pvt. Ltd..


🧩 Code Modules Overview

1️⃣ data_preprocessing.py

Purpose:
Simulates realistic production data for multiple industrial products and calculates key manufacturing KPIs.

Key Features:

Simulates production data across:
15 industrial products
3 shifts (Morning, Afternoon, Night)
Multiple production days


Generates metrics such as:
Total units produced
Rejected units
Run time & downtime
Energy consumption

Calculates Overall Equipment Effectiveness (OEE):
Availability
Performance
Quality

Saves dataset as:
production_data_15_products.csv

Run:
python data_preprocessing.py


2️⃣ ml_model.py

Purpose:
Trains a Machine Learning model to predict production downtime.

Model Details
Algorithm: Random Forest Regressor

Input Features:
Total Units Produced
Rejected Units
Energy Consumption (kWh)

Target Variable:
Downtime Minutes

Outputs:
RMSE evaluation score

Saved trained model:
downtime_model.pkl

Run:
python ml_model.py


3️⃣ visualization.py

Purpose:
Generates analytical visualizations for production insights.
Visual Outputs Created:
Total Units Produced per Product
Average OEE Trend
Correlation Heatmap of Production Metrics
OEE Distribution
Total Downtime per Product


Saved Graph Files:

units_per_product.png
monthly_oee_trend.png
correlation_heatmap.png
oee_distribution.png
downtime_per_product.png

Run:
python visualization.py

4️⃣ dashboard_app.py

Purpose:
Provides an interactive web dashboard for production monitoring and downtime prediction.
Dashboard Features:
Product & shift-based filtering

KPI summary:

Total units produced
Rejected units
Average OEE
Total downtime


Interactive charts:

OEE distribution
Units produced per product
Machine Learning-based downtime prediction using user inputs


Run Dashboard:
streamlit run dashboard_app.py


📂 Project Structure

📁 production-efficiency-system
│── data_preprocessing.py
│── ml_model.py
│── visualization.py
│── dashboard_app.py
│── production_data_15_products.csv
│── downtime_model.pkl
│── *.png
│── README.md


🛠️ Technologies Used

Python

Pandas & NumPy – Data handling
Scikit-learn – Machine Learning
Matplotlib & Seaborn – Data visualization
Streamlit – Interactive dashboard
Joblib – Model persistence


🚀 How to Run the Full Pipeline

python data_preprocessing.py
python ml_model.py
python visualization.py
streamlit run dashboard_app.py


🎯 Use Cases

Manufacturing performance monitoring
Production efficiency analysis
Downtime prediction using ML
Industrial reporting dashboards


📌 Future Enhancements

Real-time data ingestion from IoT/PLC systems
Advanced ML models (XGBoost, LSTM)
Database integration (MySQL / PostgreSQL)
Cloud deployment of Streamlit dashboard


