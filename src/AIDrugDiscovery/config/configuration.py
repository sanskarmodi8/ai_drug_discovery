from pathlib import Path

from AIDrugDiscovery.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from AIDrugDiscovery.entity.config_entity import DataIngestionConfig
from AIDrugDiscovery.utils.common import create_directories, read_yaml


class ConfigurationManager:
    def __init__(self):
        """
        Constructor for ConfigurationManager class.

        This constructor reads the configuration file and params file to create the final configuration for each step.
        """

        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        """
        This method returns the configuration for the data ingestion step.

        Returns:
            DataIngestionConfig: An object containing configuration for the data ingestion step.
        """
        create_directories(
            [self.config.data_ingestion.root_dir, self.config.data_ingestion.unzip_dir]
        )
        return DataIngestionConfig(
            root_dir=Path(self.config.data_ingestion.root_dir),
            source_url=self.config.data_ingestion.source_url,
            unzip_dir=Path(self.config.data_ingestion.unzip_dir),
        )
