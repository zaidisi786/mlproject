
import os
import sys
import numpy as np
import pandas as pd
import dill

sys.path.append('C:\\Projects\\mlproject')

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        # ensure directory exists
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # open and write the actual file path (not the directory)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)
            