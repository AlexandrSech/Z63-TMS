# Generated by Django 4.0 on 2022-02-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task21', '0002_alter_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(help_text='Введите аозраст', verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(help_text='Введите имя', max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(help_text='Введите фамилию', max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='person',
            name='profession',
            field=models.CharField(default='No info', help_text='Введите профессию', max_length=100, verbose_name='Профессия'),
        ),
    ]