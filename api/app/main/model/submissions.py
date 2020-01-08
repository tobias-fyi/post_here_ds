from .. import db

class Submission(db.Model):
    id = db.Column(db.Integer, primary)
    return_count = db.Column(db.Integer, nullable=False)
    post_body = db.Column(db.Text, nullable=False)