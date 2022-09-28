import os
from random import random
import mlflow

from mlflow import log_metric, log_param
from mlflow import log_artifacts, log_metrics, log_params

if __name__ == "__main__":
    print("======Running mlflow_tracking.py======")

    # log 개별 저장.
    # log_param("param1", randint(0, 1000))
    # log_metric("foo", random())
    # log_metric("foo", random() + 1)
    # log_metric("foo", random() + 2)

    # log JSON 형태로 한방에 저장
    model_metrics = {"model_metrics1": random(), "model_metrics2": random(),
                     "model_metrics3": random()}
    model_params = {"model_params1": random(), "model_params2": random(),
                    "model_params3": random()}

    log_metrics(model_metrics)
    log_params(model_params)

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")

    log_artifacts("outputs")

    print('tracking complete! save in ' + mlflow.active_run().info.run_uuid)
    print('command "mlflow ui"')
