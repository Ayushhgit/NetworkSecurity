from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """Data Ingestion Artifact Entity"""
    trained_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    """Data Validation Artifact Entity"""
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drft_report_file_path:str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str