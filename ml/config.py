"""
Smart Energy Bus V2
Configuration File
"""

import os

# =====================================================
# PROJECT PATHS
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "EV_Energy_Consumption_Dataset_V2.csv"
)

MODEL_FOLDER = os.path.join(
    BASE_DIR,
    "models"
)

# =====================================================
# DATASET
# =====================================================

TARGET_COLUMN = "Energy_Consumption_kWh"

DROP_COLUMNS = [
    TARGET_COLUMN
]

# =====================================================
# TRAINING
# =====================================================

TEST_SIZE = 0.20

RANDOM_STATE = 42

# =====================================================
# FEATURE TYPES
# =====================================================

CATEGORICAL_FEATURES = [

    "Driving_Mode",

    "Road_Type",

    "Traffic_Condition",

    "Road_Gradient",

    "Weather_Condition",

    "Wind"

]

# Numerical columns are detected automatically.

# =====================================================
# FEATURE ENGINEERING
# =====================================================

AVERAGE_PASSENGER_WEIGHT = 70

GRADIENT_VALUES = {

    "Descending": -4,

    "Flat": 0,

    "Ascending": 4

}

WIND_SPEED_VALUES = {

    "Low": 2,

    "Medium": 6,

    "High": 10

}

# =====================================================
# RANDOM FOREST
# =====================================================

RF_ESTIMATORS = 200

# =====================================================
# GRADIENT BOOSTING
# =====================================================

GB_RANDOM_STATE = RANDOM_STATE

# =====================================================
# XGBOOST
# =====================================================

XGB_ESTIMATORS = 100

XGB_MAX_DEPTH = 6

XGB_LEARNING_RATE = 0.1

XGB_RANDOM_STATE = RANDOM_STATE

XGB_N_JOBS = -1

# =====================================================
# VISUALIZATION
# =====================================================

FIGURE_SIZE = (10, 6)

TOP_FEATURES = 10