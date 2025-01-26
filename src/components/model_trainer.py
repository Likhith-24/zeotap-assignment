from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
from src.logger import logging

class ModelTrainer:
    def __init__(self, train_features, test_features):
        self.train_features = train_features
        self.test_features = test_features

    def train_model(self):
        logging.info("Starting model training")
        kmeans = KMeans(n_clusters=4, random_state=42)
        kmeans.fit(self.train_features)

        # Evaluate on train data
        train_clusters = kmeans.predict(self.train_features)
        train_db_index = davies_bouldin_score(self.train_features, train_clusters)

        # Evaluate on test data
        test_clusters = kmeans.predict(self.test_features)
        test_db_index = davies_bouldin_score(self.test_features, test_clusters)

        logging.info(f"Model training completed. Train DB Index: {train_db_index}, Test DB Index: {test_db_index}")
        return kmeans, train_db_index, test_db_index