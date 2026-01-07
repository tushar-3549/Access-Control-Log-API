# access_control/views.py

from rest_framework import generics
from .models import AccessLog
from .serializers import AccessLogSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AccessLogListCreateAPIView(generics.ListCreateAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['card_id']  

class AccessLogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
