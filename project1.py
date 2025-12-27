import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Create Transport Data
# -----------------------------
data = {
    "Vehicle_Type": ["Bus", "Truck", "Car", "Bike", "Auto"],
    "Trips_Per_Day": [120, 90, 300, 450, 200],
    "Fuel_Used_Liters": [480, 720, 600, 180, 220],
    "Distance_km": [2400, 3600, 3000, 1800, 1600]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. NumPy Calculations
# -----------------------------
fuel = np.array(df["Fuel_Used_Liters"])
distance = np.array(df["Distance_km"])

avg_fuel = np.mean(fuel)
max_distance = np.max(distance)
min_distance = np.min(distance)

df["Fuel_Efficiency_km_per_L"] = np.round(distance / fuel, 2)

# -----------------------------
# 3. Display Analysis
# -----------------------------
print("===== TRANSPORT ANALYZER REPORT =====\n")
print(df)

print("\nAverage Fuel Used (Liters):", avg_fuel)
print("Maximum Distance Covered (km):", max_distance)
print("Minimum Distance Covered (km):", min_distance)

# -----------------------------
# 4. Visualization
# -----------------------------

# Bar Chart - Distance Covered
plt.figure()
plt.bar(df["Vehicle_Type"], df["Distance_km"])
plt.title("Distance Covered by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Distance (km)")
plt.show()

# Line Chart - Fuel Efficiency
plt.figure()
plt.plot(df["Vehicle_Type"], df["Fuel_Efficiency_km_per_L"], marker='o')
plt.title("Fuel Efficiency of Vehicles")
plt.xlabel("Vehicle Type")
plt.ylabel("Km per Liter")
plt.show()

# Pie Chart - Fuel Consumption
plt.figure()
plt.pie(df["Fuel_Used_Liters"], labels=df["Vehicle_Type"], autopct="%1.1f%%")
plt.title("Fuel Consumption Distribution")
plt.show()