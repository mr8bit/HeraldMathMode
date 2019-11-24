from django.contrib import admin
from .models import User, Request
from backend.schedule.models import Issue, AnswerOnIssue
# Register your models here.
admin.site.register(User)
admin.site.register(Request)
admin.site.register(Issue)
admin.site.register(AnswerOnIssue)