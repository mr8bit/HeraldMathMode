from rest_framework import serializers

from backend.schedule.models import Help


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['user', 'message', 'date', 'category']