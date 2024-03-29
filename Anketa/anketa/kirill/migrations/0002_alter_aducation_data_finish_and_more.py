# Generated by Django 4.0.4 on 2022-05-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kirill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aducation',
            name='data_finish',
            field=models.DateField(blank=True, null=True, verbose_name='Окончание учебы'),
        ),
        migrations.AlterField(
            model_name='aducation',
            name='data_start',
            field=models.DateField(verbose_name='Начало учебы'),
        ),
        migrations.AlterField(
            model_name='aducation',
            name='progress',
            field=models.TextField(verbose_name='Успехи'),
        ),
        migrations.AlterField(
            model_name='hard',
            name='hard_skills',
            field=models.CharField(max_length=50, verbose_name='Хардскилл'),
        ),
        migrations.AlterField(
            model_name='work',
            name='data_finish',
            field=models.DateField(blank=True, null=True, verbose_name='Окончание работы'),
        ),
        migrations.AlterField(
            model_name='work',
            name='data_start',
            field=models.DateField(verbose_name='Начало работы'),
        ),
        migrations.AlterField(
            model_name='work',
            name='tasks',
            field=models.TextField(verbose_name='Задачи'),
        ),
    ]
