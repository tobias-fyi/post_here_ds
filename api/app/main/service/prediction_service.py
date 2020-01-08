from traceback import format_exc
import pandas as pd

def make_prediction(data):
    """
    Model will go here
    """
    try:
        dummy = {"name":['askreddit', 'funny', 'learnpython', 'datascience', 'learnprogramming'],
                    "proba":[0.12332, 0.116558, 0.78855, 0.63144, 0.21144]}
        n = data['return_count']
        text = data['submission_text']

        response_object = {'predictions': pd.DataFrame(dummy).head(n).to_dict(orient='records')}

        return response_object, 201

    except Exception:
        tb = format_exc()
        response_object = {
            'status': 'fail',
            'message': tb,
        }

        return response_object, 409


