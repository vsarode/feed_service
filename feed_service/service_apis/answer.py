from flask_restful import Resource
from flask import request, jsonify

from feed_service.service_apis_handler import answer_post_handler, \
    answer_get_handler
from feed_service.utils import answer_utils


class Answer(Resource):
    def post(self):
        request_data = request.get_json()
        answer_object = answer_post_handler.create_answer(request_data)
        response_dict = answer_utils.get_answer_dict(answer_object)
        return jsonify({"answer" : response_dict})
    def get(self):
        request_data = request.args
        if "questionId" in request_data:
            answer_object = answer_get_handler.get_answer_for_question(request_data["questionId"])
        else:
            answer_object = answer_get_handler.get_all_answer()

        answer_objects =[answer_utils.get_answer_dict(x) for x in answer_object]
        type(answer_object)
        return jsonify({"answers": answer_objects })
