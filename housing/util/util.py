import yaml
from housing.exception import HousingException
import os, sys

def read_yaml_file(file_path:str) -> dict:
    """
    Reads a yaml file and returns the content as a dictionary
    """
    try:
        config_info = None
        with open(file_path, "rb") as yaml_file:
            config_info = yaml.safe_load(yaml_file)
    
    except Exception as e:
        raise HousingException(e, sys) from e