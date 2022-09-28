from random import random


def service():
    model_metrics = {"model_metrics1": random(), "model_metrics2": random(),
                     "model_metrics3": random()}
    model_params = {"model_params1": random(), "model_params2": random(),
                    "model_params3": random()}
    return model_metrics, model_params
