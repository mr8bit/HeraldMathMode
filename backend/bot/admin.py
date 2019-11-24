from django.contrib import admin

from backend.schedule.models import Issue, AnswerOnIssue
from .models import User, Request

# Register your models here.
admin.site.register(User)
admin.site.register(Request)
admin.site.register(Issue)
admin.site.register(AnswerOnIssue)
