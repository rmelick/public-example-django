from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from quickstart.data import Status
from quickstart.serializers import UserSerializer, GroupSerializer, StatusSerializer
from quickstart.tasks import example_celery_task


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class WebserverStatus(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        serializer = StatusSerializer(Status("ok"))
        return Response(serializer.data)


class TriggerCeleryTask(APIView):
    def post(self, request):
        example_celery_task.delay()
        serializer = StatusSerializer(Status("created celery task"))
        return Response(serializer.data)
