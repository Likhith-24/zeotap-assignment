from src.utils import load_data
from src.logger import logging

class DataIngestion:
    def __init__(self, artifacts_path):
        self.artifacts_path = artifacts_path

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion")
        customers = load_data(f"{self.artifacts_path}/data/Customers.csv")
        products = load_data(f"{self.artifacts_path}/data/Products.csv")
        transactions = load_data(f"{self.artifacts_path}/data/Transactions.csv")
        train_data = load_data(f"{self.artifacts_path}/data/train.csv")
        test_data = load_data(f"{self.artifacts_path}/data/test.csv")
        logging.info("Data ingestion completed")
        return customers, products, transactions, train_data, test_data