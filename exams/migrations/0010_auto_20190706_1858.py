# Generated by Django 2.2.2 on 2019-07-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_auto_20190706_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(related_name='tests', to='exams.Question', verbose_name='question'),
        ),
    ]
