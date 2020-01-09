from traceback import format_exc
import pandas as pd
from ...subreddit_classifier.subreddit_predictor import predict


def make_prediction(data):
    """
    Model will go here
    """
    try:
        n = data['return_count']
        text = data['submission_text']
        response = predict(text, n)

        response_object = {'predictions': response}

        return response_object, 201

    except Exception:
        tb = format_exc()
        response_object = {
            'status': 'fail',
            'message': tb,
        }

        return response_object, 409


