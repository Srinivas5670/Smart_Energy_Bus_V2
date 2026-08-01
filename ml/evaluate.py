"""
Smart Energy Bus V2
Model Evaluation
"""

import os
import numpy as np
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from config import MODEL_FOLDER


def evaluate_models(
    models,
    X_test,
    y_test
):
    """
    Evaluate all trained models.
    """

    print("\n==============================")
    print("Model Performance")
    print("==============================")

    results = []

    for name, model in models.items():

        prediction = model.predict(X_test)

        mae = mean_absolute_error(
            y_test,
            prediction
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_test,
                prediction
            )
        )

        r2 = r2_score(
            y_test,
            prediction
        )

        print(f"\n{name}")
        print(f"MAE : {mae:.4f}")
        print(f"RMSE: {rmse:.4f}")
        print(f"R²  : {r2:.4f}")

        results.append({

            "Model": name,

            "MAE": mae,

            "RMSE": rmse,

            "R2": r2

        })

    results_df = pd.DataFrame(results)

    os.makedirs(
        MODEL_FOLDER,
        exist_ok=True
    )

    results_df.to_csv(

        os.path.join(
            MODEL_FOLDER,
            "model_comparison.csv"
        ),

        index=False

    )

    print("\nModel comparison saved successfully.")

    return results_df