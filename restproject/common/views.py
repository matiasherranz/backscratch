
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets

from common.models import BackScratcher
from common.serializers import (
    UserSerializer, GroupSerializer, BackScratcherSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BackScratcherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows back scratchers to be viewed or edited.
    """
    model = BackScratcher
    queryset = BackScratcher.objects.all()
    serializer_class = BackScratcherSerializer
    http_method_names = ('get', 'put', 'post', 'update')
