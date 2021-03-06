from rest_framework import serializers
from . import models

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = (
            "name",
            "contentid",
            "city",
            "address",
            "mapx",
            "mapy",
            "writer",
        )
