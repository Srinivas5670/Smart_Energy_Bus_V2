"""
Smart Energy Bus V2
Machine Learning Models
"""

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

from sklearn.svm import SVR

from sklearn.neighbors import KNeighborsRegressor

from xgboost import XGBRegressor

from config import (
    RANDOM_STATE,
    RF_ESTIMATORS,
    GB_RANDOM_STATE,
    XGB_ESTIMATORS,
    XGB_MAX_DEPTH,
    XGB_LEARNING_RATE,
    XGB_RANDOM_STATE,
    XGB_N_JOBS
)


def build_models(preprocessor):

    models = {

        "Linear Regression": Pipeline([

            ("preprocessor", preprocessor),

            ("model", LinearRegression())

        ]),

        "Random Forest": Pipeline([

            ("preprocessor", preprocessor),

            ("model",

                RandomForestRegressor(

                    n_estimators=RF_ESTIMATORS,

                    random_state=RANDOM_STATE

                )

            )

        ]),

        "Gradient Boosting": Pipeline([

            ("preprocessor", preprocessor),

            ("model",

                GradientBoostingRegressor(

                    random_state=GB_RANDOM_STATE

                )

            )

        ]),

        "XGBoost": Pipeline([

            ("preprocessor", preprocessor),

            ("model",

                XGBRegressor(

                    n_estimators=XGB_ESTIMATORS,

                    max_depth=XGB_MAX_DEPTH,

                    learning_rate=XGB_LEARNING_RATE,

                    random_state=XGB_RANDOM_STATE,

                    n_jobs=XGB_N_JOBS

                )

            )

        ]),

        "SVR": Pipeline([

            ("preprocessor", preprocessor),

            ("model", SVR())

        ]),

        "KNN": Pipeline([

            ("preprocessor", preprocessor),

            ("model", KNeighborsRegressor())

        ])

    }

    return models