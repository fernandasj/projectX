# Generated by Django 2.2.2 on 2019-07-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20190706_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='students',
            field=models.ManyToManyField(related_name='disciplines', to='core.Student', verbose_name='student'),
        ),
    ]