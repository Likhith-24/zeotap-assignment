from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from src.components.model_predictor import ModelPredictor
from src.logger import logging

class PredictPipeline:
    def __init__(self, artifacts_path, model):
        self.artifacts_path = artifacts_path
        self.model = model

    def run_pipeline(self, input_data):
        logging.info("Starting prediction pipeline")
        # Data Ingestion
        data_ingestion = DataIngestion(self.artifacts_path)
        _, _, _, _, test_data = data_ingestion.initiate_data_ingestion()

        # Data Transformation
        data_transformation = DataTransformation(test_data, input_data)
        _, input_features = data_transformation.preprocess_data()

        # Model Prediction
        predictions = self.model.predict(input_features)
        logging.info("Prediction pipeline completed")
        return predictions