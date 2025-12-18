import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):
    # ---- Fig 3a: Total Units Produced per Product ----
    plt.figure(figsize=(12,6))
    units_df = df.groupby('Product')['Total_Units_Produced'].sum().reset_index()
    sns.barplot(x='Product', y='Total_Units_Produced', data=units_df)
    plt.xticks(rotation=90)
    plt.title('Total Units Produced per Product')
    plt.ylabel('Total Units Produced')
    plt.tight_layout()
    plt.savefig('units_per_product.png')
    plt.close()
    
    # ---- Fig 3b: Monthly Average OEE Trend ----
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_oee = df.groupby('Date')['OEE'].mean().reset_index()
    plt.figure(figsize=(12,6))
    sns.lineplot(x='Date', y='OEE', data=monthly_oee, marker='o')
    plt.title('Monthly Average OEE Trend')
    plt.xticks(rotation=45)
    plt.ylabel('Average OEE')
    plt.tight_layout()
    plt.savefig('monthly_oee_trend.png')
    plt.close()
    
    # ---- Fig 3c: Correlation Heatmap ----
    plt.figure(figsize=(10,8))
    corr_cols = ['Total_Units_Produced','Rejected_Units','Downtime_Minutes','Energy_Consumption_kWh','OEE']
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Production Metrics')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    plt.close()
    
    # ---- Fig 3d: OEE Distribution ----
    plt.figure(figsize=(10,6))
    sns.histplot(df['OEE'], bins=20, kde=True, color='skyblue')
    plt.title('OEE Distribution Across All Products')
    plt.xlabel('OEE')
    plt.ylabel('Frequency')
    plt.savefig('oee_distribution.png')
    plt.close()

    # ---- Fig 3e: Downtime per Product ----
    plt.figure(figsize=(12,6))
    downtime_df = df.groupby('Product')['Downtime_Minutes'].sum().reset_index()
    sns.barplot(x='Product', y='Downtime_Minutes', data=downtime_df, palette='Reds')
    plt.xticks(rotation=90)
    plt.title('Total Downtime per Product')
    plt.ylabel('Downtime (Minutes)')
    plt.tight_layout()
    plt.savefig('downtime_per_product.png')
    plt.close()

    print("All visualizations saved: units_per_product.png, monthly_oee_trend.png, correlation_heatmap.png, oee_distribution.png, downtime_per_product.png")

if __name__ == "__main__":
    df = pd.read_csv('production_data_15_products.csv')
    create_visualizations(df)
