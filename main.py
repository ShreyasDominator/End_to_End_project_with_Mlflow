# first adding the data-ingestion pipeline
from Mlflow_ML_project import logger
from Mlflow_ML_project.pipeline.stage_01_Data_ingestion import DataIngestionTrainingPipeline
from Mlflow_ML_project.pipeline.stage_02_Data_Validation import DataValidationTrainingPipeline
from Mlflow_ML_project.pipeline.stage_03_data_Transformation import DataTransformationTrainingPipeline
from Mlflow_ML_project.pipeline.stage_04_Model_training import ModelTrainerTrainingPipeline
from Mlflow_ML_project.pipeline.stage_05_Model_Evaluation import ModelEvaluationTrainingPipeline
import os

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/ShreyasDominator/End_to_End_project_with_Mlflow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "ShreyasDominator"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "c79b27cd042d93400b3a1099115f3899a027693f"


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

STAGE_NAME=" Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME=" Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



