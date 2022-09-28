import os
import mlflow
from mlflow import log_artifacts, log_metrics, log_params
from service import service


# mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root artifacts


def tracking(tracking_uri, experiment_name):
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)

    model_metrics, model_params = service()
    log_metrics(model_metrics)
    log_params(model_params)

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")

    log_artifacts("outputs")


if __name__ == "__main__":
    print("======Running mlflow_tracking.py======")

    MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
    EXPERIMENT = 'hjm'

    tracking(MLFLOW_TRACKING_URI, EXPERIMENT)
    print('tracking complete! save in ' + mlflow.active_run().info.run_uuid)
    print('command "mlflow ui"')
