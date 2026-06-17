from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.entity.config_entity import DataIngestionConfig
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
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e , sys)