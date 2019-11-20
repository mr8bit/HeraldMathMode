from backend.schedule.models import Help
from backend.schedule.serializers import HelpSerializer
from rest_framework import viewsets


class HelpViewSet(viewsets.ModelViewSet):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
