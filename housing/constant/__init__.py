import os
from datetime import datetime

ROOT_DIR = os.getcwd() # to get current working directory

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# ---------------TRAINING PIPELINE---------------
TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'