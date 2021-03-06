from django.db import models

# Create your models here.

class Provinsi(models.Model):
    nama = models.CharField(max_length=40)
    deskripsi = models.TextField(null=True)

    def __str__(self):
        return self.nama


class Destinasi(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()
    alamat = models.TextField()
    provinsi_id = models.ForeignKey(Provinsi, on_delete=models.CASCADE, null=True)
    situs = models.URLField( blank = True)
    telepon = models.CharField(max_length=15,blank = True)
    gambar_url = models.URLField(blank = True)
    

    def __str__(self):
        return self.nama