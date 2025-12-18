import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from math import sqrt

def train_downtime_model(df):
    features = ['Total_Units_Produced','Rejected_Units','Energy_Consumption_kWh']
    X = df[features]
    y = df['Downtime_Minutes']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    print("RMSE for downtime prediction:", round(rmse,2))

    # Save model
    joblib.dump(model, 'downtime_model.pkl')
    print("Model saved as downtime_model.pkl")
    return model

if __name__ == "__main__":
    df = pd.read_csv('production_data_15_products.csv')
    train_downtime_model(df)
