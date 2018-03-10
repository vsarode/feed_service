
from flask import request, jsonify
from flask_restful import Resource

from feed_service.service_apis_handler import upvote_post_handler, \
    upvote_delete_handler
from feed_service.utils import upvote_utils


class Upvote(Resource):
    def post(self):
        request_data = request.get_json()
        upvote_object = upvote_post_handler.create_upvote(request_data)
        response_dict = upvote_utils.get_upvote_dict(upvote_object)
        return jsonify({"upvote":response_dict})
    def delete(self):
        request_data = request.get_json()
        upvote_object = upvote_delete_handler.delete_upvote(request_data)
        return jsonify({"upvote":upvote_utils.get_upvote_dict(upvote_object)})


