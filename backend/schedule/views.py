from backend.schedule.models import Issue
from backend.schedule.serializers import IssueSerializer
from rest_framework import viewsets
from rest_framework import generics


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
