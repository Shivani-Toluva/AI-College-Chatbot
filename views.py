import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from django.http import JsonResponse
from django.shortcuts import render

from .models import Question, Response
from .nlp import get_intent_from_message   

def home(request):
    return render(request, "index.html")

def safe_response(reply, image="", link=""):
    return JsonResponse({
        "response": reply,
        "image": image,
        "link": link
    })


def fallback_response(message):

    message = message.lower()

    if any(word in message for word in ["fee", "fees", "cost", "price"]):
        return "Fees vary by course. UG: ₹30k–₹60k | PG: ₹50k–₹80k.", "", ""

    if any(word in message for word in ["admission", "apply", "register", "join"]):
        return "Admissions are open. You can apply through the official portal.", "", ""

    if any(word in message for word in ["course", "program", "degree"]):
        return "We offer multiple UG and PG programs across various departments.", "", ""

    if any(word in message for word in ["contact", "phone", "email"]):
        return "You can contact us via the official college website.", "", ""

    if any(word in message for word in ["location", "where", "address"]):
        return "Our college is located in a well-equipped modern campus.", "", ""

    return "I can help you with admissions, courses, fees, placements, and contact details.", "", ""


def get_best_match(user_message, questions):

    try:
        if not questions:
            return None

        corpus = list(questions)
        corpus.append(user_message)

        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(corpus)

        similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

        best_index = np.argmax(similarity)
        best_score = similarity[0][best_index]

        if best_score > 0.4:
            return questions[best_index]

        return None

    except Exception as e:
        print("TF-IDF ERROR:", e)
        return None
def chatbot_response(request):

    try:
        user_message = request.GET.get("message", "").strip().lower()

        if not user_message:
            return safe_response("Please enter a message.")

        # Default fallback
        bot_reply, image, link = fallback_response(user_message)

        intent = get_intent_from_message(user_message)

        if intent:
            response_obj = Response.objects.filter(intent=intent).first()

            if response_obj:
                return safe_response(
                    response_obj.answer,
                    response_obj.image or "",
                    response_obj.link or ""
                )
            
        questions = list(Question.objects.values_list("text", flat=True))

        best_match = get_best_match(user_message, questions)

        if best_match:
            matched_q = Question.objects.filter(text__iexact=best_match).first()

            if matched_q:
                response_obj = Response.objects.filter(intent=matched_q.intent).first()

                if response_obj:
                    return safe_response(
                        response_obj.answer,
                        response_obj.image or "",
                        response_obj.link or ""
                    )

        return safe_response(bot_reply, image, link)

    except Exception as e:
        print("ERROR:", e)
        return safe_response("Server temporarily unavailable. Please try again.")