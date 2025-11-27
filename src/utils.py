
import os
import sys
import numpy as np
import pandas as pd
import dill  # library to help crete pkl filr
from sklearn.metrics import r2_score

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

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for name, model in models.items():
            # train the model
            model.fit(X_train, y_train)

            # predict the train and test data
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # train, test model scores
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)          
        