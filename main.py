# first adding the data-ingestion pipeline
from Mlflow_ML_project import logger
from Mlflow_ML_project.pipeline.stage_01_Data_ingestion import DataIngestionTrainingPipeline

logger.info('Welcome to our custom logging')
STAGE_NAME=" Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
