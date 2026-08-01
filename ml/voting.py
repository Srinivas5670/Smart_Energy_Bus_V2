"""
Smart Energy Bus V2
Voting Regressor
"""

from sklearn.ensemble import VotingRegressor


def build_voting_regressor(
    models,
    X_train,
    y_train
):
    """
    Build, train and return the Voting Regressor.
    """

    voting = VotingRegressor(

        estimators=[

            (

                "Random Forest",

                models["Random Forest"]

            ),

            (

                "Gradient Boosting",

                models["Gradient Boosting"]

            ),

            (

                "XGBoost",

                models["XGBoost"]

            )

        ]

    )

    print("\nTraining Voting Regressor...")

    voting.fit(

        X_train,

        y_train

    )

    print("Voting Regressor Completed.")

    return voting