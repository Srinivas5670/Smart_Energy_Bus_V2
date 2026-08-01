"""
Smart Energy Bus V2
Main Training Script
"""

from dataset import load_dataset
from preprocess import preprocess_data
from models import build_models
from voting import build_voting_regressor
from evaluate import evaluate_models
from visualization import generate_visualizations
from save_models import save_all_models
from utils import print_header


def main():

    print_header("SMART ENERGY BUS V2 - MODEL TRAINING")

    # -------------------------------------------------
    # Load Dataset
    # -------------------------------------------------

    (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor
    ) = load_dataset()

    # -------------------------------------------------
    # Feature Engineering
    # -------------------------------------------------

    X_train, X_test = preprocess_data(
        X_train,
        X_test
    )

    # -------------------------------------------------
    # Build Models
    # -------------------------------------------------

    models = build_models(preprocessor)

    # -------------------------------------------------
    # Train Models
    # -------------------------------------------------

    print("\nTraining Models...\n")

    for name, model in models.items():

        print(f"Training {name}...")

        model.fit(
            X_train,
            y_train
        )

        print(f"{name} Completed\n")

    # -------------------------------------------------
    # Voting Regressor
    # -------------------------------------------------

    voting_model = build_voting_regressor(
        models,
        X_train,
        y_train
    )

    models["Voting Regressor"] = voting_model

    # -------------------------------------------------
    # Evaluate Models
    # -------------------------------------------------

    results_df = evaluate_models(
        models,
        X_test,
        y_test
    )

    # -------------------------------------------------
    # Save Models
    # -------------------------------------------------

    save_all_models(
        models,
        results_df
    )

    # -------------------------------------------------
    # Generate Charts
    # -------------------------------------------------

    generate_visualizations(
        results_df,
        models
    )

    print("\nTraining Completed Successfully.")


if __name__ == "__main__":
    main()