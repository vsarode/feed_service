from feed_service.db.feed_models.models import Upvote
from feed_service.service_apis_handler import answer_get_handler
from feed_service.utils.exceptions import InternalServerError


def create_upvote(request_data):
    user_id = request_data['userId']
    answer_id = request_data['answerId']

    answer_object = answer_get_handler.get_answer_by_id(answer_id)

    try:
        upvote_object,is_created = Upvote.objects.get_or_create(user_id = user_id, answer = answer_object)
        return upvote_object

    except Exception as e:
        print e
        raise InternalServerError()
