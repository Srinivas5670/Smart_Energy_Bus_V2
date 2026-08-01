"""
Smart Energy Bus V2
Dataset Loader
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from config import (
    DATASET_PATH,
    TARGET_COLUMN,
    DROP_COLUMNS,
    TEST_SIZE,
    RANDOM_STATE,
    CATEGORICAL_FEATURES
)


def load_dataset():

    print("\nLoading Dataset...")

    # -------------------------------------------------
    # Read Dataset
    # -------------------------------------------------

    df = pd.read_csv(DATASET_PATH)

    print(df.head())
    print(df.info())

    # -------------------------------------------------
    # Cleaning
    # -------------------------------------------------

    df.drop_duplicates(inplace=True)

    df.ffill(inplace=True)

    # -------------------------------------------------
    # Features & Target
    # -------------------------------------------------

    X = df.drop(columns=DROP_COLUMNS)

    y = df[TARGET_COLUMN]

    # -------------------------------------------------
    # Numerical Features
    # -------------------------------------------------

    numerical_features = [

        column

        for column in X.columns

        if column not in CATEGORICAL_FEATURES

    ]

    # -------------------------------------------------
    # Preprocessor
    # -------------------------------------------------

    preprocessor = ColumnTransformer(

        transformers=[

            (

                "num",

                StandardScaler(),

                numerical_features

            ),

            (

                "cat",

                OneHotEncoder(
                    handle_unknown="ignore"
                ),

                CATEGORICAL_FEATURES

            )

        ]

    )

    # -------------------------------------------------
    # Train Test Split
    # -------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=TEST_SIZE,

        random_state=RANDOM_STATE

    )

    print("\nDataset Loaded Successfully.")

    print(f"Training Samples : {len(X_train)}")

    print(f"Testing Samples  : {len(X_test)}")

    return (

        X_train,

        X_test,

        y_train,

        y_test,

        preprocessor

    )