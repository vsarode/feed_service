from feed_service.db.feed_models.models import Question


def create_question(request_data):
    user_name = request_data['userId']
    question_string = request_data['questionString']

    try:
        question_object = Question.objects.create(user_id=user_name,
                                                  question_string=question_string)
        return question_object
    except Exception as e:
        print e
        return None
