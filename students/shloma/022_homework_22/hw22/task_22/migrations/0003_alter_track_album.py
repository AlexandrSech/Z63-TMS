# Generated by Django 4.0 on 2022-02-14 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_22', '0002_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='task_22.album'),
        ),
    ]
