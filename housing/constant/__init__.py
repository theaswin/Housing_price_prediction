
import os
from datetime import datetime
ROOT_DIR = os.getcwd() # to get current working dir

CONFIG_DIR = 'config'
CONFIG_FILE_NAME = 'config.yaml'
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME) # usr/config/config.yaml

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}" # current time stamp

# Training pipeline related varables
TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'


# Data ingestion related variable
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

# Data validation related variable
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_ARTIFACT_DIR_NAME="data_validation"
DATA_VALIDATION_REPORT_FILE_NAME_KEY = "report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = "report_page_file_name"


# Data transformation related variable
DATA_TRANSFORMATION_ARTIFACT_DIR = "data_transformation"
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY = "add_bedroom_per_room"
DATA_TRANSFORMATION_DIR_NAME_KEY =  "transformed_dir"
DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY = "transformed_train_dir"
DATA_TRANSFORMATION_TEST_DIR_NAME_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY = "preprocessed_object_file_name"

# Model training config key
MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY = "trained_model_dir"
MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY = "model_file_name"
MODEL_TRAINER_BASE_ACCURACY_KEY = "base_accuracy"
MODEL_TRAINER_MODEL_CONFIG_DIR_KEY = "model_config_dir"
MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY = "model_config_file_name"

# Model evaluation config key
MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_FILE_NAME_KEY = "model_evaluation_file_name"
MODEL_EVALUATION_ARTIFACT_DIR = "model_evaluation"

# Model Pusher config key
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_PUSHER_MODEL_EXPORT_DIR_KEY = "model_export_dir"