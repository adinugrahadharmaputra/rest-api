# Generated by Django 3.2 on 2021-04-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('deskripsi', models.TextField()),
                ('gambar_url', models.URLField()),
                ('provinsi', models.CharField(max_length=50)),
                ('alamat', models.TextField()),
                ('situs', models.URLField()),
                ('jam_buka', models.TimeField()),
                ('jam_tutup', models.TimeField()),
            ],
        ),
    ]