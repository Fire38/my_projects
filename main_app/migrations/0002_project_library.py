# Generated by Django 2.0.10 on 2019-01-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='library',
            field=models.TextField(default='pass'),
        ),
    ]