from flask_restful import Resource
import json
from flask import request, session, make_response

from feed_service.services import user_service


class Login(Resource):
    def post(self):
        request_data = request.get_json()
        user_dict = user_service.login(request_data['username'],
                                       request_data['password'],
                                       request_data['clientId'])
        session['key'] = user_dict['authToken']
        user_dict = user_dict['user']
        session['username'] = user_dict['username']
        session['phone'] = user_dict['phone']
        session['lastName'] = user_dict['lastName']
        session['email'] = user_dict['email']

        response = make_response(json.dumps(user_dict))
        response.set_cookie("auth_key", session['key'])
        response.mimetype = "application/json"

        print "session==>", session
        return response

