"""
Smart Energy Bus V2
Model Saving Module
"""

import os
import joblib

from config import MODEL_FOLDER


def save_all_models(
    models,
    results_df=None
):
    """
    Save all trained models.
    """

    os.makedirs(
        MODEL_FOLDER,
        exist_ok=True
    )

    model_files = {

        "Linear Regression": "linear.pkl",

        "Random Forest": "random_forest.pkl",

        "Gradient Boosting": "gradient_boost.pkl",

        "XGBoost": "xgboost.pkl",

        "SVR": "svr.pkl",

        "KNN": "knn.pkl",

        "Voting Regressor": "voting.pkl"

    }

    print("\nSaving Models...\n")

    for model_name, filename in model_files.items():

        if model_name not in models:
            continue

        filepath = os.path.join(
            MODEL_FOLDER,
            filename
        )

        joblib.dump(
            models[model_name],
            filepath
        )

        print(f"✓ {filename} saved.")

    print("\nAll models saved successfully.")