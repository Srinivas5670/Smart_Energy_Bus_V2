"""
Smart Energy Bus V2
Feature Engineering Module
"""

from config import (
    AVERAGE_PASSENGER_WEIGHT,
    GRADIENT_VALUES,
    WIND_SPEED_VALUES
)


# =====================================================
# Vehicle Features
# =====================================================

def calculate_effective_vehicle_weight(
    vehicle_weight,
    passenger_count
):
    """
    Calculate total vehicle weight including passengers.
    """

    return vehicle_weight + (
        passenger_count * AVERAGE_PASSENGER_WEIGHT
    )


# =====================================================
# Road Gradient
# =====================================================

def gradient_to_value(gradient):
    """
    Convert Road Gradient category to model value.
    """

    return GRADIENT_VALUES.get(
        gradient,
        0
    )


# =====================================================
# Wind
# =====================================================

def wind_to_value(wind):
    """
    Convert Wind category to representative speed.
    """

    return WIND_SPEED_VALUES.get(
        wind,
        6
    )


# =====================================================
# Battery Estimation
# =====================================================

def estimate_remaining_battery(
    battery_percentage,
    predicted_energy,
    battery_capacity=250
):
    """
    Estimate remaining battery percentage.

    battery_capacity is in kWh.
    """

    battery_used = (
        predicted_energy / battery_capacity
    ) * 100

    remaining = battery_percentage - battery_used

    return max(0, round(remaining, 2))


# =====================================================
# Future
# =====================================================

def estimate_battery_voltage(
    battery_percentage
):
    """
    Placeholder for future voltage estimation.
    """

    if battery_percentage >= 80:
        return 400

    if battery_percentage >= 60:
        return 390

    if battery_percentage >= 40:
        return 380

    if battery_percentage >= 20:
        return 370

    return 360