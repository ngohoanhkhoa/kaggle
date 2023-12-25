"""
This is a boilerplate pipeline 'pipeline_digits'
generated using Kedro 0.18.13
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import get_dataset, split_dataset, fit_model, predict_data

def create_pipeline(**kwargs) -> Pipeline:
    pipeline_ex = [node(
        func=get_dataset,
        inputs=None,
        outputs="raw_data"),
        node(
            func=split_dataset,
            inputs=["raw_data", "params:test_size"],
            outputs=["X_train", "X_test", "y_train", "y_test"]
        ),
        node(
            func=fit_model,
            inputs=["X_train", "y_train", "params:epochs", "params:batch_size"],
            outputs="model"
        ),
        node(
            func=predict_data,
            inputs=["model", "X_test", "params:batch_size"],
            outputs="y_predict"
        )]

    return pipeline(pipeline_ex)