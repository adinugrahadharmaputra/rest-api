# Generated by Django 3.2 on 2021-04-20 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=20)),
                ('jam_buka', models.TimeField()),
                ('jam_tutup', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='destinasi',
            name='jam_buka',
        ),
        migrations.RemoveField(
            model_name='destinasi',
            name='jam_tutup',
        ),
        migrations.AddField(
            model_name='destinasi',
            name='telepon',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='destinasi',
            name='jam_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='destinasi.jam'),
        ),
    ]