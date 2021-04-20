from destinasi.models import Provinsi
from rest_framework import serializers

class PovinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinsi
        fields = ['id', 'nama', 'deskripsi']