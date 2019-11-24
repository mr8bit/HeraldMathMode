from rest_framework import serializers

from backend.schedule.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'user', 'message', 'date', 'category', 'has_answer']


