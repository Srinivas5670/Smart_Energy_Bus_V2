import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:

    # =====================================================
    # Flask
    # =====================================================

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "SmartEnergyBusV2_2026_SecureKey"
    )


    DEBUG = os.environ.get("FLASK_DEBUG", "False") == "True"

    # =====================================================
    # Database
    # =====================================================

    DATABASE = os.path.join(
        BASE_DIR,
        "database",
        "energy_bus.db"
    )

    # =====================================================
    # JWT
    # =====================================================

    JWT_EXPIRATION_HOURS = 245555

    # =====================================================
    # ML Models
    # =====================================================

    PROJECT_ROOT = os.path.dirname(BASE_DIR)

    MODEL_FOLDER = os.path.join(
        PROJECT_ROOT,
        "models"
    )

    # =====================================================
    # Battery
    # =====================================================

    BATTERY_CAPACITY_KWH = 250

    AVERAGE_PASSENGER_WEIGHT = 70