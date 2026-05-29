from django.contrib import admin
from .models import Intent, Question, Response

admin.site.register(Intent)
admin.site.register(Question)
admin.site.register(Response)
