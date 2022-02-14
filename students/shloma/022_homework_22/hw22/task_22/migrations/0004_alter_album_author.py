# Generated by Django 4.0 on 2022-02-14 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_22', '0003_alter_track_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='task_22.musicband'),
        ),
    ]
