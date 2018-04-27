from django.shortcuts import render
from rest_framework import mixins, viewsets, serializers

from piano.models import Piano
from piano.serializers import PianoSerializer


class PianoViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Piano.objects.all()
    serializer_class = PianoSerializer
