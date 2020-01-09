# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.prediction_controller import api as pred_ns
from .subreddit_classifier.models import load_mvp

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API FOR NLP PREDICTIONS',
          version='0.2.1',
          description='subreddit classification via machine learning'
          )

api.add_namespace(pred_ns, path='/predict')

# vocab, nb, le = load_mvp()