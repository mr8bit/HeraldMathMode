import datetime

from django.db.models import Count
from rest_framework import generics
from rest_framework import viewsets

from backend.admin.serializers import RequestSerializer, RequestStateCountsSerializer, NotificationSerializer
from backend.bot.models import Request, Notification


class RequestList(generics.ListAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self):
        type = self.kwargs['type']
        if type == "month":
            return Request.objects.filter(date__month=datetime.datetime.now().month)
        if type == "day":
            return Request.objects.filter(date__day=datetime.datetime.now().day)
        if type == "week":
            date = datetime.date.today()
            start_week = date - datetime.timedelta(date.weekday())
            end_week = start_week + datetime.timedelta(7)
            return Request.objects.filter(date__range=[start_week, end_week])
        if type == "range":
            start = self.request.query_params.get('start', None)
            end = self.request.query_params.get('end', None)
            start = datetime.datetime.strptime(start, '%d.%m.%Y').date()
            end = datetime.datetime.strptime(end, '%d.%m.%Y').date()
            return Request.objects.filter(date__range=[start, end])


class RequestGroupByList(generics.ListAPIView):
    serializer_class = RequestStateCountsSerializer

    def get_queryset(self):
        type = self.kwargs['type']
        if type == "month":
            return Request.objects.filter(date__month=datetime.datetime.now().month).values('state').annotate(
                dcount=Count('state'))
        if type == "day":
            return Request.objects.filter(date__day=datetime.datetime.now().day).values('state').annotate(
                dcount=Count('state'))
        if type == "week":
            date = datetime.date.today()
            start_week = date - datetime.timedelta(date.weekday())
            end_week = start_week + datetime.timedelta(7)
            return Request.objects.filter(date__range=[start_week, end_week]).values('state').annotate(
                dcount=Count('state'))
        if type == "range":
            start = self.request.query_params.get('start', None)
            end = self.request.query_params.get('end', None)
            start = datetime.datetime.strptime(start, '%d.%m.%Y').date()
            end = datetime.datetime.strptime(end, '%d.%m.%Y').date()
            return Request.objects.filter(date__range=[start, end]).values('state').annotate(
                dcount=Count('state'))


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
