"""
Smart Energy Bus V2
Visualization Module
"""

import os
import matplotlib.pyplot as plt
import pandas as pd

from config import (
    MODEL_FOLDER,
    FIGURE_SIZE,
    TOP_FEATURES
)


def generate_visualizations(
    results_df,
    models
):
    """
    Generate all visualizations.
    """

    os.makedirs(
        MODEL_FOLDER,
        exist_ok=True
    )

    create_mae_chart(results_df)

    create_rmse_chart(results_df)

    create_r2_chart(results_df)

    create_feature_importance_chart(models)


# =====================================================
# MAE Chart
# =====================================================

def create_mae_chart(results_df):

    plt.figure(figsize=FIGURE_SIZE)

    plt.bar(
        results_df["Model"],
        results_df["MAE"]
    )

    plt.title("Model Comparison - MAE")

    plt.xlabel("Models")

    plt.ylabel("MAE")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            MODEL_FOLDER,
            "mae_chart.png"
        )
    )

    plt.close()


# =====================================================
# RMSE Chart
# =====================================================

def create_rmse_chart(results_df):

    plt.figure(figsize=FIGURE_SIZE)

    plt.bar(
        results_df["Model"],
        results_df["RMSE"]
    )

    plt.title("Model Comparison - RMSE")

    plt.xlabel("Models")

    plt.ylabel("RMSE")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            MODEL_FOLDER,
            "rmse_chart.png"
        )
    )

    plt.close()


# =====================================================
# R² Chart
# =====================================================

def create_r2_chart(results_df):

    plt.figure(figsize=FIGURE_SIZE)

    plt.bar(
        results_df["Model"],
        results_df["R2"]
    )

    plt.title("Model Comparison - R² Score")

    plt.xlabel("Models")

    plt.ylabel("R²")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            MODEL_FOLDER,
            "r2_chart.png"
        )
    )

    plt.close()


# =====================================================
# Feature Importance
# =====================================================

def create_feature_importance_chart(models):

    xgb_pipeline = models["XGBoost"]

    feature_importance = (
        xgb_pipeline
        .named_steps["model"]
        .feature_importances_
    )

    feature_names = (
        xgb_pipeline
        .named_steps["preprocessor"]
        .get_feature_names_out()
    )

    importance_df = pd.DataFrame({

        "Feature": feature_names,

        "Importance": feature_importance

    })

    importance_df = importance_df.sort_values(

        by="Importance",

        ascending=False

    ).head(TOP_FEATURES)

    plt.figure(figsize=FIGURE_SIZE)

    plt.barh(

        importance_df["Feature"],

        importance_df["Importance"]

    )

    plt.xlabel("Importance Score")

    plt.ylabel("Features")

    plt.title("XGBoost Feature Importance")

    plt.tight_layout()

    plt.savefig(

        os.path.join(

            MODEL_FOLDER,

            "feature_importance.png"

        )

    )

    plt.close()

    print("\nFeature Importance chart saved successfully.")