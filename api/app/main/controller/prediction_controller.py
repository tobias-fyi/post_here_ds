from flask import request
from flask_restplus import Resource

from ..util.prediction_dto import PredictionDto
from ..service.prediction_service import make_prediction

api = PredictionDto.api
_pred = PredictionDto.preds

@api.route('/')
@api.param( 'post_body','numbers of predictions to return')
@api.param('return_count', 'int amount of predictions to return')
class Prediction(Resource):
    @api.doc('model predictions')
    @api.expect(_pred)
    def post(self):
        """subreddit classificat using machine learning"""
        data = request.json
        return make_prediction(data)