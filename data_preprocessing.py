
import pandas as pd
import random

def simulate_production_data():
    products = [
        'Welding Robotic Arm','Assembly Robotic Arm','Painting Robotic Arm',
        'Material Handling Robotic Arm','Packaging Robotic Arm','CNC Machining Robotic Arm',
        'Inspection & Testing Robotic Arm','Robotic Arm for Electronics Assembly','Collaborative Robotic Arm (Cobot)',
        'Laboratory Robotic Arm','Palletizing Robotic Arm','Custom Robotic Arm Unit',
        'Siemens Operator Panel','Industrial Encoder','Automated Conveyor System'
    ]

    shifts = ['Morning','Afternoon','Night']
    days = pd.date_range(start='2025-06-23', end='2025-07-11')
    data = []

    for date in days:
        for shift in shifts:
            for product in products:
                total_units = random.randint(5, 20)
                rejected_units = random.randint(0, 2)
                run_time = random.randint(400, 480)
                downtime = 480 - run_time
                planned_time = 480
                operator = 'Operator_' + str(random.randint(1,10))
                energy = round(run_time/60 * random.uniform(10, 25), 2)
                data.append([
                    date, shift, product, total_units, rejected_units,
                    run_time, downtime, planned_time, operator, energy
                ])

    df = pd.DataFrame(data, columns=[
        'Date','Shift','Product','Total_Units_Produced','Rejected_Units',
        'Run_Time_Minutes','Downtime_Minutes','Planned_Production_Time','Operator_Name','Energy_Consumption_kWh'
    ])
    
    # Calculate OEE
    df['Availability'] = df['Run_Time_Minutes'] / df['Planned_Production_Time']
    df['Quality'] = (df['Total_Units_Produced'] - df['Rejected_Units']) / df['Total_Units_Produced']
    df['Performance'] = df['Total_Units_Produced'] / (df['Run_Time_Minutes']/60 * 5)
    df['OEE'] = df['Availability'] * df['Performance'] * df['Quality']

    df.to_csv('production_data_15_products.csv', index=False)
    print("Data simulation complete. Saved to production_data_15_products.csv")
    return df

if __name__ == "__main__":
simulate_production_data()
