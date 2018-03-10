from feed_service.db.feed_models.models import Answer
from feed_service.service_apis_handler import question_get_handler
from feed_service.utils.exceptions import InternalServerError


def create_answer(request_data):
    user_id = request_data['userId']
    question_id = request_data['questionId']
    answer_string = request_data['answerString']
    question_object = question_get_handler.get_question_by_id(question_id)
    try:
        answer_object = Answer.objects.create(user_id=user_id,
                                              answer_string=answer_string,
                                              question=question_object)
        return answer_object
    except:
        raise InternalServerError()
   