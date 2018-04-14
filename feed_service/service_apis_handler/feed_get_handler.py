from feed_service.db.feed_models.models import Question, Answer
from feed_service.utils import answer_utils





def get_question_to_answer_map(answers):
    question_to_answer_map = {}

    for answer in answers:
        if answer.question in question_to_answer_map:
            question_to_answer_map[answer.question].append(answer)
        else:
            question_to_answer_map[answer.question] = [answer]

    return question_to_answer_map

def get_answer_to_upvote_downvote_map(answers):
    answer_to_upvote_downvote_map = {}
    for answer in answers:
        upvote_downvote = (answer.upvote_set.count(), answer.downvote_set.count())
        answer_to_upvote_downvote_map[answer] = upvote_downvote
    return answer_to_upvote_downvote_map

def get_feed_data():

    qsn_list = []
    questions = Question.objects.all()
    all_answers = Answer.objects.all().prefetch_related('question');
    question_to_answers_map = get_question_to_answer_map(all_answers);
    answer_to_upvote_downvote_count = get_answer_to_upvote_downvote_map(all_answers)

    for question in questions:
        answers_for_question  = question_to_answers_map[question] if question in question_to_answers_map else []
        answerList = []
        for answer in answers_for_question:
            ans_dict = answer_utils.get_answer_dict(answer)

            upvote_count = answer_to_upvote_downvote_count[answer][0]
            downvote_count = answer_to_upvote_downvote_count[answer][1]

            ans_dict['upvoteCount'] = upvote_count
            ans_dict['downvoteCount'] = downvote_count
            ans_dict.pop('question')
            answerList.append(ans_dict)

        q_dict = {}
        q_dict['questionString'] = question.question_string
        q_dict['userId'] = question.user_id
        q_dict['all_answers'] = answerList
        qsn_list.append(q_dict)
    return qsn_list