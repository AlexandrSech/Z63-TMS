# Generated by Django 4.0 on 2022-02-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_24', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natureimage',
            name='link',
            field=models.CharField(help_text='Input image link', max_length=500, null=True, verbose_name='Link'),
        ),
    ]
