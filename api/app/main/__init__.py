from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name


db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)
    db.init_app(app)

    return app
















    # @app.route("/", methods=['POST'])
    # def address():
    #     '''Takes json dictionaries and return prediction values'''
    #     # unpickle model
    #     # receive input
    #     inputs = request.get_json(force=True)        
        
    #     # assign variables
    #     body = inputs['post_body']

        
    #     # wrangle input        
    #     # predict
    #     dummy = {"name":['askreddit', 'funny', 'learnpython', 'datascience', 'learnprogramming'],
    #             "proba":[0.12332, 0.116558, 0.78855, 0.63144, 0.21144]}        
        
    #     # format for json return
    #     out = {'predictions': pd.DataFrame(dummy).to_dict(orient='records')}
        
    #     # give output to sender
    #     return app.response_class(
    #         response=json.dumps(out),
    #         status=200,
    #         mimetype='application/json')

    # return app

# if __name__ == '__main__':
#     app.run(port=9000, debug=True)
