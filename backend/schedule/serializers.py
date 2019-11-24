from rest_framework import serializers

from backend.schedule.models import Issue, AnswerOnIssue


class AnswerOnIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOnIssue
        fields = ['id', 'issue', 'text', 'date']


class IssueSerializer(serializers.ModelSerializer):
    answers = AnswerOnIssueSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'user', 'message', 'date', 'category', 'has_answer', 'answers']
