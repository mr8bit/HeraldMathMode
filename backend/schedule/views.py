from rest_framework import viewsets

from backend.schedule.models import Issue, AnswerOnIssue
from backend.schedule.serializers import IssueSerializer, AnswerOnIssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class AnswerOnIssueViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', ]
    queryset = AnswerOnIssue.objects.all()
    serializer_class = AnswerOnIssueSerializer

