
from django.urls import path
from .views import AccessLogListCreateAPIView, AccessLogRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('logs/', AccessLogListCreateAPIView.as_view(), name='accesslog-list-create'),
    path('logs/<int:pk>/', AccessLogRetrieveUpdateDestroyAPIView.as_view(), name='accesslog-detail'),
]
