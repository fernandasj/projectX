# Generated by Django 2.2.2 on 2019-07-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20190706_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='students',
            field=models.ManyToManyField(default=[], related_name='disciplines', to='core.Student', verbose_name='students'),
        ),
    ]