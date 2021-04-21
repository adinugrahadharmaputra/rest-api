from destinasi.models import Destinasi, Provinsi
from rest_framework import serializers

class DestinasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinasi
        fields = ['id','nama','deskripsi','alamat','provinsi_id','situs','telepon','gambar_url']


class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinasi
        fields = ['id','nama','deskripsi']