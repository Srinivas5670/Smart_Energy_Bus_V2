from services.model_service import model_service

sample_input = {
    "Speed_kmh": 60,
    "Acceleration_ms2": 1.5,
    "Battery_State_%": 80,
    "Battery_Voltage_V": 390,
    "Battery_Temperature_C": 30,
    "Driving_Mode": 1,
    "Road_Type": 2,
    "Traffic_Condition": 1,
    "Slope_%": 2,
    "Weather_Condition": 0,
    "Temperature_C": 28,
    "Humidity_%": 65,
    "Wind_Speed_ms": 3,
    "Tire_Pressure_psi": 35,
    "Vehicle_Weight_kg": 1800,
    "Distance_Travelled_km": 25
}

result = model_service.predict(sample_input)

print(result)