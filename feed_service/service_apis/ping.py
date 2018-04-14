import json

from flask import make_response, request, session
from flask_restful import Resource


class Ping(Resource):
    def get(self):

        return {"Message": "welcome to feed service !!!"}

    def post(self, id):
        d = request.get_json()
        session[id] = d
        print session[id]
