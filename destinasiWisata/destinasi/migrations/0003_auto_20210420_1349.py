# Generated by Django 3.2 on 2021-04-20 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinasi', '0002_auto_20210420_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='destinasi',
            name='jam_id',
        ),
        migrations.RemoveField(
            model_name='destinasi',
            name='provinsi',
        ),
        migrations.DeleteModel(
            name='Jam',
        ),
        migrations.AddField(
            model_name='destinasi',
            name='provinsi_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='destinasi.provinsi'),
        ),
    ]