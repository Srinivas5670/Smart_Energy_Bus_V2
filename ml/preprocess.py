"""
Smart Energy Bus V2
Preprocessing & Feature Engineering
"""

try:
    from ml.config import (
        AVERAGE_PASSENGER_WEIGHT,
        GRADIENT_VALUES,
        WIND_SPEED_VALUES
    )
except ImportError:
    from config import (
        AVERAGE_PASSENGER_WEIGHT,
        GRADIENT_VALUES,
        WIND_SPEED_VALUES
    )


def preprocess_data(X_train, X_test):
    """
    Apply feature engineering before model training.
    """

    X_train = X_train.copy()
    X_test = X_test.copy()

    # Convert Road Gradient
    X_train["Road_Gradient"] = X_train["Road_Gradient"].map(
        GRADIENT_VALUES
    )

    X_test["Road_Gradient"] = X_test["Road_Gradient"].map(
        GRADIENT_VALUES
    )

    # Convert Wind Category
    X_train["Wind"] = X_train["Wind"].map(
        WIND_SPEED_VALUES
    )

    X_test["Wind"] = X_test["Wind"].map(
        WIND_SPEED_VALUES
    )

    # Effective Vehicle Weight
    X_train["Vehicle_Weight_kg"] = (
        X_train["Vehicle_Weight_kg"]
        + X_train["Passenger_Count"] * AVERAGE_PASSENGER_WEIGHT
    )

    X_test["Vehicle_Weight_kg"] = (
        X_test["Vehicle_Weight_kg"]
        + X_test["Passenger_Count"] * AVERAGE_PASSENGER_WEIGHT
    )

    return X_train, X_test


# =====================================================
# Helper Functions
# =====================================================

def calculate_effective_vehicle_weight(
    vehicle_weight,
    passenger_count
):
    return vehicle_weight + (
        passenger_count * AVERAGE_PASSENGER_WEIGHT
    )


def gradient_to_value(gradient):
    return GRADIENT_VALUES.get(
        gradient,
        0
    )


def wind_to_value(wind):
    return WIND_SPEED_VALUES.get(
        wind,
        6
    )


def estimate_remaining_battery(
    battery_percentage,
    predicted_energy,
    battery_capacity=250
):
    battery_used = (
        predicted_energy / battery_capacity
    ) * 100

    remaining = battery_percentage - battery_used

    return max(
        0,
        round(remaining, 2)
    )


def estimate_battery_voltage(
    battery_percentage
):
    if battery_percentage >= 80:
        return 400

    if battery_percentage >= 60:
        return 390

    if battery_percentage >= 40:
        return 380

    if battery_percentage >= 20:
        return 370

    return 360