import os
import zipfile
from abc import ABC, abstractmethod

import gdown

from AIDrugDiscovery import logger
from AIDrugDiscovery.entity.config_entity import DataIngestionConfig


class DataIngestionAbstract(ABC):
    def __init__(self, config: DataIngestionConfig):
        """
        Constructor for DataIngestionAbstract class.

        Args:
            config (DataIngestionConfig): The configuration for the data ingestion step.
        """
        self.config = config

    @abstractmethod
    def download_data(self):
        """
        Abstract method to download data using the given config.
        """
        pass


class GDriveDataIngestion(DataIngestionAbstract):
    def download_data(self):
        """
        Downloads data from the given Google Drive URL and extracts it into the given directory.

        Raises:
            Exception: If there is an error while downloading or extracting the data.
        """
        config = self.config
        if os.path.exists(config.unzip_dir) and len(os.listdir(config.unzip_dir)) > 0:
            logger.info(
                f"Data already exists in {config.unzip_dir}. Skipping download."
            )
        else:
            try:
                dataset_url = config.source_url
                zip_download_path = config.root_dir / "data.zip"
                logger.info(
                    f"Downloading data from {dataset_url} into file {zip_download_path}"
                )

                file_id = dataset_url.split("/")[-2]
                prefix = "https://drive.google.com/uc?/export=download&id="

                gdown.download(prefix + file_id, str(zip_download_path))
                logger.info(
                    f"Downloaded data from {dataset_url} into file {zip_download_path}"
                )

                # extract the data
                logger.info(f"Extracting data into {config.unzip_dir}")
                with zipfile.ZipFile(zip_download_path, "r") as zip_ref:
                    zip_ref.extractall(config.unzip_dir)
                logger.info(f"Data extracted into {config.unzip_dir}")

            except Exception as e:
                logger.error(
                    f"Error occurred while downloading or extracting the data: {e}"
                )
                raise e


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        """
        Constructor for DataIngestion class.

        Args:
            config (DataIngestionConfig): The configuration for the data ingestion step.
        """
        self.config = config
        self.factory = self.get_factory()

    def get_factory(self) -> DataIngestionAbstract:
        """
        Factory method to return the appropriate DataIngestion class
        """
        if self.config.source_url.startswith("https://drive.google.com"):
            return GDriveDataIngestion(self.config)
        else:
            # Here, we can extend this logic for other sources like AWS S3, HTTP URLs, etc.
            raise ValueError("Unsupported data source URL")

    def run(self):
        """
        Method to run the data ingestion step.
        """
        self.factory.download_data()
