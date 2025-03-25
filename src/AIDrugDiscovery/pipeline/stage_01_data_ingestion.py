from AIDrugDiscovery import logger
from AIDrugDiscovery.components.data_ingestion import DataIngestion
from AIDrugDiscovery.config.configuration import ConfigurationManager

STAGE_NAME = "DATA INGESTION STAGE"


class DataIngestionPipeline:
    def __init__(self):
        """
        This special method is the Constructor for this class.

        This method creates an instance of the `DataIngestionPipeline` class.
        The instance is created from the configuration manager's data ingestion config.
        """
        self.config = ConfigurationManager().get_data_ingestion_config()
        self.data_ingestion = DataIngestion(self.config)

    def main(self):
        """
        This method starts the data ingestion stage.
        """
        self.data_ingestion.run()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
