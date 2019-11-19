from rest_framework import serializers

from backend.bot.models import Request, Notification


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'user', 'state', 'date', 'text']


class RequestStateCountsSerializer(serializers.ModelSerializer):
    dcount = serializers.IntegerField()

    class Meta:
        model = Request
        fields = ['state', 'dcount']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['name', 'message', 'for_messenger']
