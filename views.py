from django.shortcuts import render
from django.db.models import Count

from chatbott.models import Intent, Question, Response


# =========================
# DASHBOARD HOME
# =========================
def dashboard_home(request):

    # Total data counts
    total_intents = Intent.objects.count()
    total_questions = Question.objects.count()
    total_responses = Response.objects.count()

    # Most used intents (based on questions)
    top_intents = (
        Question.objects.values('intent__name')
        .annotate(count=Count('intent'))
        .order_by('-count')[:5]
    )

    context = {
        "total_intents": total_intents,
        "total_questions": total_questions,
        "total_responses": total_responses,
        "top_intents": top_intents,
    }

    return render(request, "dashboard/dashboard.html", context)