from dataclasses import dataclass
from pathlib import Path

# entity classes for each configuration


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    unzip_dir: Path
