import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.logger import logging

class DataTransformation:
    def __init__(self, train_data, test_data):
        self.train_data = train_data
        self.test_data = test_data

    def preprocess_data(self):
        logging.info("Starting data transformation")
        # Preprocess train data
        train_features = self._create_features(self.train_data)
        test_features = self._create_features(self.test_data)

        logging.info("Data transformation completed")
        return train_features, test_features

    def _create_features(self, data):
        # Example feature engineering
        features = data.groupby("CustomerID").agg({
            "TotalValue": ["sum", "mean"],
            "Quantity": ["sum", "mean"],
            "Region": "first",
            "Category": lambda x: x.mode()[0]
        }).reset_index()

        # Flatten multi-level columns
        features.columns = ["CustomerID", "TotalValueSum", "TotalValueMean", "QuantitySum", "QuantityMean", "Region", "FavoriteCategory"]

        # Encode categorical variables
        encoder = OneHotEncoder()
        encoded_region = encoder.fit_transform(features[["Region"]]).toarray()
        encoded_category = encoder.fit_transform(features[["FavoriteCategory"]]).toarray()

        # Combine features
        numerical_features = features[["TotalValueSum", "TotalValueMean", "QuantitySum", "QuantityMean"]]
        scaler = StandardScaler()
        scaled_numerical = scaler.fit_transform(numerical_features)
        final_features = pd.concat([
            pd.DataFrame(scaled_numerical),
            pd.DataFrame(encoded_region),
            pd.DataFrame(encoded_category)
        ], axis=1)

        return final_features