from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging

class TrainPipeline:
    def __init__(self, artifacts_path):
        self.artifacts_path = artifacts_path

    def run_pipeline(self):
        logging.info("Starting training pipeline")
        # Data Ingestion
        data_ingestion = DataIngestion(self.artifacts_path)
        customers, products, transactions, train_data, test_data = data_ingestion.initiate_data_ingestion()

        # Data Transformation
        data_transformation = DataTransformation(train_data, test_data)
        train_features, test_features = data_transformation.preprocess_data()

        # Model Training
        model_trainer = ModelTrainer(train_features, test_features)
        model, train_db_index, test_db_index = model_trainer.train_model()

        logging.info("Training pipeline completed")
        return model, train_db_index, test_db_index