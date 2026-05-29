import re
from difflib import get_close_matches
from .models import Question


def clean(text):
    return re.sub(r'[^a-z0-9\s]', '', text.lower()).strip()


def get_intent_from_message(user_message):

    user_message = clean(user_message)

    questions = Question.objects.all()

    question_map = {
        clean(q.text): q.intent for q in questions
    }

    question_list = list(question_map.keys())

    # =============================
    # 1. KEYWORD MATCH
    # =============================
    for q in question_list:
        q_words = set(q.split())
        u_words = set(user_message.split())

        if len(u_words.intersection(q_words)) >= 1:
            return question_map[q]

    # =============================
    # 2. FUZZY MATCH
    # =============================
    match = get_close_matches(user_message, question_list, n=1, cutoff=0.4)

    if match:
        return question_map[match[0]]

    return None