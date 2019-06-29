# Generated by Django 2.2.2 on 2019-06-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20190603_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='codeanswer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='discipline',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='test',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='teststudent',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]