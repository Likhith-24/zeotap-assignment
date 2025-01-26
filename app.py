from src.pipeline.train_pipeline import TrainPipeline
from src.logger import logging

if __name__ == "__main__":
    try:
        logging.info("Starting the application")
        train_pipeline = TrainPipeline(artifacts_path="artifacts")
        model, train_db_index, test_db_index = train_pipeline.run_pipeline()
        logging.info(f"Model trained successfully. Train DB Index: {train_db_index}, Test DB Index: {test_db_index}")
    except Exception as e:
        logging.error(f"Error in application: {e}")