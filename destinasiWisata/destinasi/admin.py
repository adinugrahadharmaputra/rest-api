from django.contrib import admin
from destinasi.models import Destinasi,Provinsi

# Register your models here.
class DestinasiAdmin(admin.ModelAdmin):
    list_display = ['nama','deskripsi','alamat','provinsi_id','situs','telepon','gambar_url']
    search_fields = ['nama','deskripsi','alamat']
    list_filter = ('provinsi_id',)
    list_per_page = 4

admin.site.register(Destinasi, DestinasiAdmin)
admin.site.register(Provinsi)

