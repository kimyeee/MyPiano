# coding: utf-8
from rest_framework import serializers

from piano.models import Piano


class PianoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piano
        fields = ['artist', 'name']