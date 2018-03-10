from flask import request, jsonify
from flask_restful import Resource

from feed_service.service_apis_handler import question_post_handler, \
    question_get_handler
from feed_service.utils import question_utils


class Question(Resource):
    def post(self):
        request_data = request.get_json()
        result = question_post_handler.create_question(request_data)
        if result:
            response_dict = question_utils.get_question_dict(result)
            return jsonify({"question": response_dict})
        else:
            return {"success": False}

    def get(self, user_id=None):
        if user_id:
            question_objects = question_get_handler.get_question_for_user(
                user_id)
        else:
            question_objects = question_get_handler.get_all_questions()

        response_dicts = [question_utils.get_question_dict(x)
                          for x in question_objects]
        return jsonify({"questions": response_dicts})
