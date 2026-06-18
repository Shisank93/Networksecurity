from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.components.data_validation import DataValidation
from Networksecurity.entity.config_entity import DataIngestionConfig , DataValidationConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig


from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
import sys



if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)  ## initialising data injetion or make object 
        logging.info("Initiate the data injestion")
        dataingestionartifact=  data_ingestion.initiate_data_ingestion()
        logging.info("data initiation completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(dataingestionartifact ,data_validation_config=data_validation_config)
        logging.info("initiated data validation")
        data_validation_artifact =data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
        

    except Exception as e:
        raise NetworkSecurityException(e , sys)